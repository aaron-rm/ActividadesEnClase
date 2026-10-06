# -*- coding: utf-8 -*-
"""
red.py
------
Networking del modo Online. Radmin VPN crea una red virtual (LAN)
entre las computadoras conectadas a ella: una vez que ambos jugadores
están en la misma red de Radmin VPN, se pueden ver entre sí por IP
exactamente igual que si estuvieran en la misma red local. Por eso acá
alcanza con un socket TCP simple: no hace falta ningún servidor
intermedio ni NAT traversal.

Roles:
  - Host  : abre un socket y espera una conexión entrante. Juega con X
            (jugador índice 0).
  - Unirse: se conecta a la IP de Radmin VPN del host. Juega con O
            (jugador índice 1).

Protocolo: mensajes JSON de una línea (terminados en "\n") sobre el
socket TCP. Tipos de mensaje:
  {"tipo": "jugada", "x": .., "y": .., "z": ..}
  {"tipo": "reinicio"}
  {"tipo": "desconectado"}   (generado localmente, no viaja por la red)
"""

import json
import queue
import socket
import threading
import time

# Puerto TCP por defecto para el modo Online. Se puede cambiar desde el
# menú si hiciera falta (por ejemplo, si ya está en uso).
PUERTO_DEFECTO = 5050

# Puerto UDP usado solo para el "descubrimiento" de partidas abiertas:
# el host difunde por broadcast que está esperando rival, y cualquier
# otra PC en la misma red de Radmin VPN puede escucharlo sin necesidad
# de que nadie escriba una IP a mano. Como puede haber más de una
# persona conectada a la misma red virtual, puede haber más de un host
# anunciándose al mismo tiempo.
PUERTO_DESCUBRIMIENTO = 5051


class ConexionOnline:
    """Conexión punto a punto (host <-> unido) para el modo Online."""

    def __init__(self, es_host, host="", puerto=PUERTO_DEFECTO):
        self.es_host = es_host
        self.host = host
        self.puerto = puerto

        self.sock_escucha = None   # solo lo usa el host, para el accept()
        self.conn = None           # socket ya conectado, usado por ambos roles
        self.hilo_recepcion = None

        self.cola_recibidos = queue.Queue()
        self.conectado = False
        self.error = None

    @property
    def mi_jugador(self):
        """0 (X) si soy el host, 1 (O) si me uní a un host."""
        return 0 if self.es_host else 1

    def conectar(self):
        """Establece la conexión. Es una llamada BLOQUEANTE (el host se
        queda esperando en accept() hasta que alguien se una; el que se
        une espera hasta que el host acepte o hasta que falle). Por eso
        se debe llamar desde un hilo secundario, nunca desde el hilo de
        la interfaz gráfica.

        Devuelve True si la conexión se estableció, False si falló
        (revisar `self.error` para el detalle)."""
        try:
            if self.es_host:
                print(f"[Online] Host: abriendo puerto {self.puerto} y esperando al rival...")
                self.sock_escucha = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock_escucha.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self.sock_escucha.bind(("0.0.0.0", self.puerto))
                self.sock_escucha.listen(1)
                self.conn, direccion = self.sock_escucha.accept()
                print(f"[Online] Rival conectado desde {direccion[0]}:{direccion[1]}.")
            else:
                print(f"[Online] Conectando a {self.host}:{self.puerto}...")
                self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.conn.settimeout(10.0)
                self.conn.connect((self.host, self.puerto))
                self.conn.settimeout(None)  # volver a modo bloqueante normal
                print(f"[Online] Conexión establecida con {self.host}:{self.puerto}.")
        except Exception as e:
            self.error = str(e)
            self.conectado = False
            print(f"[Online] Error al conectar: {e}")
            return False

        self.conectado = True
        self.hilo_recepcion = threading.Thread(target=self._recibir_loop, daemon=True)
        self.hilo_recepcion.start()
        return True

    def _recibir_loop(self):
        """Corre en un hilo aparte: lee mensajes JSON de a una línea y
        los deja en la cola para que la interfaz los procese cuando
        pueda (nunca se toca matplotlib/tkinter desde este hilo)."""
        buffer = b""
        while True:
            try:
                datos = self.conn.recv(4096)
            except Exception as e:
                print(f"[Online] Error recibiendo datos: {e}")
                break
            if not datos:
                print("[Online] El rival cerró la conexión.")
                break
            buffer += datos
            while b"\n" in buffer:
                linea, buffer = buffer.split(b"\n", 1)
                if not linea.strip():
                    continue
                try:
                    mensaje = json.loads(linea.decode("utf-8"))
                    self.cola_recibidos.put(mensaje)
                except Exception:
                    pass  # ignoramos líneas corruptas en vez de romper la conexión

        self.conectado = False
        print("[Online] Conexión finalizada.")
        self.cola_recibidos.put({"tipo": "desconectado"})

    def enviar_jugada(self, x, y, z):
        self._enviar({"tipo": "jugada", "x": x, "y": y, "z": z})

    def enviar_reinicio(self):
        self._enviar({"tipo": "reinicio"})

    def enviar_chat(self, texto):
        print(f"[Online] Chat enviado: {texto}")
        self._enviar({"tipo": "chat", "texto": texto})

    def _enviar(self, mensaje):
        if not self.conectado or self.conn is None:
            return
        try:
            linea = (json.dumps(mensaje) + "\n").encode("utf-8")
            self.conn.sendall(linea)
        except Exception as e:
            self.conectado = False
            print(f"[Online] Error enviando datos: {e}")

    def obtener_mensajes_pendientes(self):
        """Vacía y devuelve todos los mensajes recibidos hasta ahora
        (no bloqueante), para que la interfaz los procese en su propio
        ciclo de refresco."""
        mensajes = []
        while True:
            try:
                mensajes.append(self.cola_recibidos.get_nowait())
            except queue.Empty:
                break
        return mensajes

    def cerrar(self):
        """Cierra los sockets. Si el host estaba bloqueado en accept(),
        esto lo libera con un error (lo cual es la forma de cancelar la
        espera desde la interfaz)."""
        print("[Online] Cerrando conexión...")
        self.conectado = False
        for sock in (self.conn, self.sock_escucha):
            try:
                if sock is not None:
                    sock.close()
            except Exception:
                pass


# ----------------------------------------------------------------------
# Descubrimiento de partidas abiertas (UDP broadcast)
# ----------------------------------------------------------------------
# Radmin VPN puede tener a MÁS de dos personas conectadas a la misma red
# virtual. Para no obligar a escribir la IP a mano, mientras el host
# espera rival difunde por broadcast UDP un "acá hay una partida
# esperando"; cualquier otra PC que esté en el paso de "Unirme a un
# Host" escucha esos anuncios y arma un listado (con scroll, por si hay
# varias partidas abiertas a la vez) para elegir con qué host conectarse.
class AnunciadorPartida:
    """Corre en un hilo aparte, mientras el host espera rival, difundiendo
    por broadcast UDP que esta partida está disponible."""

    def __init__(self, puerto_juego, puerto_descubrimiento=PUERTO_DESCUBRIMIENTO, intervalo=1.0):
        self.puerto_juego = puerto_juego
        self.puerto_descubrimiento = puerto_descubrimiento
        self.intervalo = intervalo
        self.nombre = socket.gethostname()
        self._activo = False
        self._hilo = None

    def iniciar(self):
        self._activo = True
        self._hilo = threading.Thread(target=self._loop, daemon=True)
        self._hilo.start()
        print(f"[Online] Difundiendo partida '{self.nombre}' (puerto {self.puerto_juego}) "
              f"en la red para que otros la encuentren...")

    def detener(self):
        if self._activo:
            self._activo = False
            print("[Online] Se dejó de difundir la partida.")

    def _loop(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        except Exception as e:
            print(f"[Online] Error creando el socket de difusión: {e}")
            return

        mensaje = json.dumps({
            "tipo": "anuncio_partida",
            "nombre": self.nombre,
            "puerto": self.puerto_juego,
        }).encode("utf-8")

        while self._activo:
            try:
                sock.sendto(mensaje, ("255.255.255.255", self.puerto_descubrimiento))
            except Exception as e:
                print(f"[Online] Error difundiendo la partida: {e}")
            time.sleep(self.intervalo)

        try:
            sock.close()
        except Exception:
            pass


class BuscadorPartidas:
    """Corre en un hilo aparte escuchando anuncios de partidas (ver
    `AnunciadorPartida`) y los va dejando en una cola para que la
    interfaz arme un listado (puede haber varias partidas abiertas a la
    vez si hay más de dos personas en la misma red de Radmin VPN)."""

    def __init__(self, puerto_descubrimiento=PUERTO_DESCUBRIMIENTO):
        self.puerto_descubrimiento = puerto_descubrimiento
        self.cola_encontrados = queue.Queue()
        self._activo = False
        self._hilo = None
        self._sock = None

    def iniciar(self):
        self._activo = True
        self._hilo = threading.Thread(target=self._loop, daemon=True)
        self._hilo.start()
        print(f"[Online] Buscando partidas abiertas en la red (puerto UDP {self.puerto_descubrimiento})...")

    def detener(self):
        if self._activo:
            self._activo = False
            print("[Online] Se detuvo la búsqueda de partidas.")
        if self._sock is not None:
            try:
                self._sock.close()
            except Exception:
                pass

    def _loop(self):
        try:
            self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self._sock.bind(("0.0.0.0", self.puerto_descubrimiento))
            self._sock.settimeout(1.0)
        except Exception as e:
            print(f"[Online] Error escuchando anuncios de partidas: {e}")
            return

        while self._activo:
            try:
                datos, (ip, _puerto_origen) = self._sock.recvfrom(2048)
            except socket.timeout:
                continue
            except Exception:
                break
            try:
                mensaje = json.loads(datos.decode("utf-8"))
            except Exception:
                continue
            if mensaje.get("tipo") == "anuncio_partida":
                nombre = mensaje.get("nombre", "Host desconocido")
                puerto = mensaje.get("puerto", PUERTO_DEFECTO)
                print(f"[Online] Partida encontrada: '{nombre}' en {ip}:{puerto}")
                self.cola_encontrados.put({"ip": ip, "puerto": puerto, "nombre": nombre})

        try:
            self._sock.close()
        except Exception:
            pass

    def obtener_encontrados(self):
        """Vacía y devuelve todas las partidas encontradas hasta ahora
        (no bloqueante)."""
        encontrados = []
        while True:
            try:
                encontrados.append(self.cola_encontrados.get_nowait())
            except queue.Empty:
                break
        return encontrados