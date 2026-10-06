# -*- coding: utf-8 -*-
import json
import queue
import random
import socket
import threading
import time

try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    print("Error: tkinter no está instalado. Instalalo con 'pip install tk' o 'sudo apt install python3-tk' (Linux).")

try:
    import matplotlib
    matplotlib.use("TkAgg")  # backend interactivo con ventana propia

    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle
    from matplotlib.lines import Line2D
    from mpl_toolkits.mplot3d import proj3d  # noqa: F401 (necesario para proyección 3D)
    from matplotlib.widgets import Button, Slider, RadioButtons
except ImportError:
    print("Error: matplotlib no está instalado. Instalalo con 'pip install matplotlib'.")


"""
Constantes y paleta de colores compartidas por todo el proyecto:
tamaño del tablero, textos de los modos de juego y colores usados
tanto en el menú (tkinter) como en la interfaz 3D (matplotlib).
"""

# Tamaño fijo del tablero (4x4x4).
TAM = 4

# Textos descriptivos de cada modo de juego, usados en el menú y en el
# subtítulo de la ventana de juego.
MODO_TEXTO = {
    "2P": "2 Jugadores (misma compu)",
    "BOT": "Contra la Computadora",
    "ONLINE": "Online",
}

# Paleta del MENÚ (tkinter)
BG_OSCURO = "#1d3557"
BG_TARJETA = "#274668"
BG_TARJETA_HOVER = "#2f5580"
ACENTO = "#f4a300"
VERDE = "#2a9d8f"
ROJO = "#e63946"
AZUL = "#457b9d"
TEXTO_CLARO = "#f1faee"
TEXTO_TENUE = "#a8dadc"

# Paleta del TABLERO / CUBO 3D (matplotlib)
COLOR_X = "#e63946"        # rojo  - jugador X
COLOR_O = "#457b9d"        # azul  - jugador O
COLOR_LIBRE = "#c9c9c9"    # gris  - casilla libre
COLOR_GANADOR = "#2a9d8f"  # verde - línea ganadora
COLOR_HOVER = "#f4a300"    # dorado - casilla bajo el mouse

COLOR_EJE_X = "#e63946"    # rojo
COLOR_EJE_Y = "#2a9d8f"    # verde
COLOR_EJE_Z = "#457b9d"    # azul

# Un color distinto por cada capa Z: se usa tanto en el borde/título del
# tablerito 2D como en el plano equivalente dibujado dentro del cubo 3D,
# para poder identificar de un vistazo qué capa es cuál.
COLORES_CAPA = ["#e63946", "#f4a300", "#2a9d8f", "#8338ec", "#fb5607", "#3a86ff"]


def color_de_capa(z):
    """Devuelve el color asociado a la capa Z indicada (cíclico)."""
    return COLORES_CAPA[z % len(COLORES_CAPA)]



"""
Reglas puras del Tic-Tac-Toe 3D (NxNxN), sin ninguna dependencia de la
interfaz gráfica. Todo el estado de una partida vive dentro de la
clase Tablero, así que se pueden crear varias instancias (por ejemplo,
para tests) sin que se pisen entre sí.

Convención de valores en `jugadas[z][y][x]`:
    0  = libre
   -1  = X
    1  = O
"""


class Tablero:
    """Estado y reglas de una partida de Tic-Tac-Toe 3D de tamaño `tam`."""

    def __init__(self, tam):
        self.tam = tam
        self.jugadas = [[[0 for _ in range(tam)] for _ in range(tam)] for _ in range(tam)]

        self.X = self.Y = self.Z = 0   # coordenadas de la última jugada
        self.jugador = 0                # 0 = X, 1 = O
        self.g = 0                       # 0 = sigue la partida, 1 = hay ganador

    # Verificación de líneas ganadoras (usa siempre la ÚLTIMA jugada
    # como referencia: X, Y, Z)
    def horizontal(self):
        return abs(sum(self.jugadas[self.Z][self.Y])) == self.tam

    def vertical(self):
        return abs(sum(self.jugadas[self.Z][y][self.X] for y in range(self.tam))) == self.tam

    def profundidad(self):
        return abs(sum(self.jugadas[z][self.Y][self.X] for z in range(self.tam))) == self.tam

    def diagonal_xy(self):
        n = self.tam
        d1 = sum(self.jugadas[self.Z][i][i] for i in range(n))
        d2 = sum(self.jugadas[self.Z][i][n - 1 - i] for i in range(n))
        return abs(d1) == n or abs(d2) == n

    def diagonal_xz(self):
        n = self.tam
        d1 = sum(self.jugadas[i][self.Y][i] for i in range(n))
        d2 = sum(self.jugadas[i][self.Y][n - 1 - i] for i in range(n))
        return abs(d1) == n or abs(d2) == n

    def diagonal_yz(self):
        n = self.tam
        d1 = sum(self.jugadas[i][i][self.X] for i in range(n))
        d2 = sum(self.jugadas[i][n - 1 - i][self.X] for i in range(n))
        return abs(d1) == n or abs(d2) == n

    def diagonal_espacial(self):
        n = self.tam
        d1 = sum(self.jugadas[i][i][i] for i in range(n))
        d2 = sum(self.jugadas[i][i][n - 1 - i] for i in range(n))
        d3 = sum(self.jugadas[i][n - 1 - i][i] for i in range(n))
        d4 = sum(self.jugadas[n - 1 - i][i][i] for i in range(n))
        return (
            abs(d1) == n or
            abs(d2) == n or
            abs(d3) == n or
            abs(d4) == n
        )

    def verificar_ganador(self):
        return (
            self.horizontal()
            or self.vertical()
            or self.profundidad()
            or self.diagonal_xy()
            or self.diagonal_xz()
            or self.diagonal_yz()
            or self.diagonal_espacial()
        )

    # Acciones sobre el tablero
    def jugar(self, x, y, z):
        """Intenta colocar la ficha del jugador actual en (x, y, z).
        Devuelve True si la jugada fue válida y se aplicó."""
        if self.g:
            return False

        if not (0 <= x < self.tam and 0 <= y < self.tam and 0 <= z < self.tam):
            return False

        if self.jugadas[z][y][x] != 0:
            return False

        self.X, self.Y, self.Z = x, y, z
        self.jugadas[z][y][x] = -1 if self.jugador == 0 else 1

        if self.verificar_ganador():
            self.g = 1
            return True

        self.jugador = 1 - self.jugador
        return True

    def reiniciar(self):
        """Vuelve a dejar el tablero como recién creado."""
        tam = self.tam
        self.jugadas = [[[0 for _ in range(tam)] for _ in range(tam)] for _ in range(tam)]
        self.jugador = 0
        self.g = 0
        self.X = self.Y = self.Z = 0

    def tablero_lleno(self):
        return all(
            self.jugadas[z][y][x] != 0
            for x in range(self.tam) for y in range(self.tam) for z in range(self.tam)
        )

    def hay_ganador_en(self, x, y, z):
        """Evalúa si hay ganador asumiendo que la última jugada fue
        (x, y, z), sin depender de que jugar() haya sido llamado (útil
        para el bot, que necesita simular jugadas sin comprometerlas de
        verdad)."""
        x_bak, y_bak, z_bak = self.X, self.Y, self.Z
        self.X, self.Y, self.Z = x, y, z
        resultado = self.verificar_ganador()
        self.X, self.Y, self.Z = x_bak, y_bak, z_bak
        return resultado


"""
IA del bot (juega siempre como "O", jugador índice 1, pero el código es
genérico respecto a qué valor le toque). Estrategia:

  1) Si hay una jugada que gana ya, la juega.
  2) Si no, si el rival puede ganar en su próximo turno, bloquea.
  3) Si no, elige la celda con mejor puntaje heurístico (líneas propias
     abiertas + preferencia por el centro), con un poco de azar para no
     ser 100% predecible.
"""
def generar_todas_las_lineas(n):
    """Todas las líneas ganadoras posibles (mismas familias que las
    funciones de verificación de Tablero, pero para TODAS las
    capas/ejes, no solo la de la última jugada). Se usa para la
    heurística del bot."""
    lineas = []

    for z in range(n):
        for y in range(n):
            lineas.append([(x, y, z) for x in range(n)])          # horizontal
    for z in range(n):
        for x in range(n):
            lineas.append([(x, y, z) for y in range(n)])          # vertical
    for y in range(n):
        for x in range(n):
            lineas.append([(x, y, z) for z in range(n)])          # profundidad

    for z in range(n):
        lineas.append([(i, i, z) for i in range(n)])              # diagonal_xy
        lineas.append([(n - 1 - i, i, z) for i in range(n)])
    for y in range(n):
        lineas.append([(i, y, i) for i in range(n)])              # diagonal_xz
        lineas.append([(n - 1 - i, y, i) for i in range(n)])
    for x in range(n):
        lineas.append([(x, i, i) for i in range(n)])              # diagonal_yz
        lineas.append([(x, n - 1 - i, i) for i in range(n)])

    lineas.append([(i, i, i) for i in range(n)])                  # diagonal espacial
    lineas.append([(i, i, n - 1 - i) for i in range(n)])
    lineas.append([(i, n - 1 - i, i) for i in range(n)])
    lineas.append([(n - 1 - i, i, i) for i in range(n)])

    return lineas


class BotIA:
    """IA del bot para un Tablero de tamaño `tablero.tam`."""

    def __init__(self, tablero):
        self.tablero = tablero
        self.tam = tablero.tam

        self.todas_las_lineas = generar_todas_las_lineas(self.tam)
        self.lineas_por_celda = {}
        for linea in self.todas_las_lineas:
            for celda in linea:
                self.lineas_por_celda.setdefault(celda, []).append(linea)

    def _puntaje_celda(self, pos, valor_jugador):
        """Cuánto conviene esa celda para `valor_jugador` (-1 o 1): suma
        el cuadrado de piezas propias en cada línea que pasa por `pos` y
        que todavía no está bloqueada por el rival."""
        jugadas = self.tablero.jugadas
        puntaje = 0
        for linea in self.lineas_por_celda.get(pos, []):
            propios = 0
            rivales = 0
            for (x, y, z) in linea:
                v = jugadas[z][y][x]
                if v == valor_jugador:
                    propios += 1
                elif v == -valor_jugador:
                    rivales += 1
            if rivales == 0:
                puntaje += propios ** 2
        return puntaje

    def movida_bot(self):
        """Elige una jugada para el bot (siempre juega con el valor que
        le corresponda al jugador actual del tablero). Devuelve una
        tupla (x, y, z), o None si no quedan celdas libres."""
        tablero = self.tablero
        jugadas = tablero.jugadas
        tam = self.tam

        valor_bot = -1 if tablero.jugador == 0 else 1
        valor_rival = -valor_bot

        libres = [
            (x, y, z)
            for z in range(tam) for y in range(tam) for x in range(tam)
            if jugadas[z][y][x] == 0
        ]
        if not libres:
            return None

        # 1) ¿Puedo ganar ya?
        for (x, y, z) in libres:
            jugadas[z][y][x] = valor_bot
            gana = tablero.hay_ganador_en(x, y, z)
            jugadas[z][y][x] = 0
            if gana:
                return (x, y, z)

        # 2) ¿Tengo que bloquear al rival?
        for (x, y, z) in libres:
            jugadas[z][y][x] = valor_rival
            gana = tablero.hay_ganador_en(x, y, z)
            jugadas[z][y][x] = 0
            if gana:
                return (x, y, z)

        # 3) Heurística
        centro = (tam - 1) / 2
        mejor = None
        mejor_puntaje = None
        for (x, y, z) in libres:
            puntaje = self._puntaje_celda((x, y, z), valor_bot)
            puntaje -= self._puntaje_celda((x, y, z), valor_rival) * 0.9
            dist_centro = abs(x - centro) + abs(y - centro) + abs(z - centro)
            puntaje -= dist_centro * 0.1
            puntaje += random.uniform(0, 0.05)  # desempate no determinista
            if mejor_puntaje is None or puntaje > mejor_puntaje:
                mejor_puntaje = puntaje
                mejor = (x, y, z)

        return mejor


# ======================================================================
# =============================  red.py  ===============================
# ======================================================================
"""
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


# ======================================================================
# =============================  menu.py  ===============================
# ======================================================================
"""
Pantalla inicial (tkinter) donde el usuario elige el modo de juego:
2 Jugadores, Contra la Computadora, u Online (Host / Unirse por
Radmin VPN).

Expone una única función pública: `elegir_configuracion()`, que abre la
ventana, la espera, y devuelve un dict:
    {"modo": "2P" | "BOT" | "ONLINE", "conexion": ConexionOnline | None}

Si el modo es "ONLINE", "conexion" ya viene conectada y lista para usar.
Si el usuario cancela el sub-flujo de Online, se cae automáticamente a
"2P" con conexion=None.
"""


def elegir_configuracion():
    """Muestra el menú inicial y devuelve
    {"modo": ..., "conexion": ConexionOnline | None}."""
    resultado = {"modo": "2P", "conexion": None}

    root = tk.Tk()
    root.title("Tic-Tac-Toe 3D | Aaron Remarchuk 2026 CLAUDE")
    root.configure(bg=BG_OSCURO)
    root.resizable(False, False)

    ancho_v, alto_v = 460, 600
    root.update_idletasks()
    ancho_p = root.winfo_screenwidth()
    alto_p = root.winfo_screenheight()
    pos_x = (ancho_p // 2) - (ancho_v // 2)
    pos_y = (alto_p // 2) - (alto_v // 2)
    root.geometry(f"{ancho_v}x{alto_v}+{pos_x}+{pos_y}")

    # --- Encabezado ---
    marco_header = tk.Frame(root, bg=BG_OSCURO)
    marco_header.pack(pady=(36, 4))
    tk.Label(marco_header, text="TIC", font=("Arial", 28, "bold"),
             fg=TEXTO_CLARO, bg=BG_OSCURO).pack(side="left")
    tk.Label(marco_header, text="·TAC·", font=("Arial", 28, "bold"),
             fg=ACENTO, bg=BG_OSCURO).pack(side="left")
    tk.Label(marco_header, text="TOE", font=("Arial", 28, "bold"),
             fg=TEXTO_CLARO, bg=BG_OSCURO).pack(side="left")

    tk.Label(root, text="3 D   ·   T A B L E R O   4 × 4 × 4",
             font=("Arial", 10), fg=TEXTO_TENUE, bg=BG_OSCURO).pack(pady=(0, 30))

    tk.Frame(root, bg="#3a5a80", height=1, width=380).pack(pady=(0, 22))

    # --- Selección de modo ---
    tk.Label(root, text="Elegí el modo de juego", font=("Arial", 12, "bold"),
              fg=TEXTO_CLARO, bg=BG_OSCURO).pack(pady=(0, 14))

    marco_modo = tk.Frame(root, bg=BG_OSCURO)
    marco_modo.pack(fill="x", padx=40)

    var_modo = tk.StringVar(value="2P")

    opciones_modo = [
        ("2 Jugadores", "Misma computadora, por turnos", "2P", VERDE),
        ("Contra el Bot", "La IA juega como \u201cO\u201d", "BOT", ROJO),
        ("Online", "Por Radmin VPN, Host o Unirse", "ONLINE", AZUL),
    ]

    botones_modo = []

    def resaltar_seleccionado(*_args):
        elegido = var_modo.get()
        for valor, boton in botones_modo:
            boton.configure(bg=BG_TARJETA_HOVER if valor == elegido else BG_TARJETA)

    for titulo, subt, valor, color in opciones_modo:
        rb = tk.Radiobutton(
            marco_modo, variable=var_modo, value=valor, command=resaltar_seleccionado,
            text=f"  {titulo}\n  {subt}", justify="left",
            font=("Arial", 11, "bold"),
            fg=TEXTO_CLARO, bg=BG_TARJETA, selectcolor=color,
            activebackground=BG_TARJETA_HOVER, activeforeground=TEXTO_CLARO,
            indicatoron=0, anchor="w", padx=14, pady=10,
            bd=0, highlightthickness=2, highlightbackground=BG_OSCURO,
            highlightcolor=color, relief="flat", cursor="hand2",
        )
        rb.pack(fill="x", pady=7)
        botones_modo.append((valor, rb))

    resaltar_seleccionado()

    def comenzar():
        modo = var_modo.get()
        if modo == "ONLINE":
            conexion = _configurar_online(root)
            if conexion is None:
                # el usuario canceló el sub-flujo (o la conexión falló):
                # nos quedamos en el menú principal, no arrancamos nada.
                return
            resultado["modo"] = "ONLINE"
            resultado["conexion"] = conexion
            root.quit()
            return

        resultado["modo"] = modo
        resultado["conexion"] = None
        root.quit()  # sale del mainloop; la ventana se destruye después

    btn_comenzar = tk.Button(
        root, text="COMENZAR", font=("Arial", 13, "bold"),
        fg="white", bg=VERDE, activebackground="#23897d", activeforeground="white",
        bd=0, pady=13, cursor="hand2", command=comenzar,
    )
    btn_comenzar.pack(fill="x", padx=40, pady=(28, 30))

    def _hover_on(_e):
        btn_comenzar.configure(bg="#23897d")

    def _hover_off(_e):
        btn_comenzar.configure(bg=VERDE)

    btn_comenzar.bind("<Enter>", _hover_on)
    btn_comenzar.bind("<Leave>", _hover_off)

    def _on_close():
        if messagebox.askokcancel("Salir", "¿Querés salir del juego?", parent=root):
            resultado["modo"] = None
            root.quit()

    root.protocol("WM_DELETE_WINDOW", _on_close)

    root.mainloop()
    root.destroy()

    return resultado


# ------------------------------------------------------------------
# Sub-flujo del modo Online: elegir Host/Unirse y conectar por
# Radmin VPN.
# ------------------------------------------------------------------
def _obtener_ips_locales():
    """Direcciones IPv4 de este equipo, para mostrarle al host cuál
    pasarle al rival. Radmin VPN suele asignar IPs que empiezan con
    "26."; si detectamos alguna la mostramos primero."""
    ips = []
    try:
        nombre_host = socket.gethostname()
        _, _, lista = socket.gethostbyname_ex(nombre_host)
        for ip in lista:
            if ip not in ips:
                ips.append(ip)
    except Exception:
        pass
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0.5)
        s.connect(("8.8.8.8", 80))
        ip_salida = s.getsockname()[0]
        s.close()
        if ip_salida not in ips:
            ips.append(ip_salida)
    except Exception:
        pass
    return ips


def _configurar_online(root):
    """Sub-flujo modal del modo Online. Devuelve una ConexionOnline ya
    conectada, o None si el usuario canceló."""
    resultado = {"conexion": None}

    # Hilos de fondo (anunciador de partida propia / buscador de partidas
    # ajenas) que hay que detener prolijamente al cambiar de paso o cerrar
    # la ventana, para no dejarlos corriendo de más.
    recursos_activos = []

    def _liberar_recursos():
        while recursos_activos:
            recurso = recursos_activos.pop()
            try:
                recurso.detener()
            except Exception:
                pass

    vent = tk.Toplevel(root)
    vent.title("Modo Online")
    vent.configure(bg=BG_OSCURO)
    vent.resizable(False, False)
    vent.transient(root)
    vent.grab_set()

    ancho_v, alto_v = 460, 560
    root.update_idletasks()
    pos_x = root.winfo_x() + (root.winfo_width() // 2) - (ancho_v // 2)
    pos_y = root.winfo_y() + (root.winfo_height() // 2) - (alto_v // 2)
    vent.geometry(f"{ancho_v}x{alto_v}+{pos_x}+{pos_y}")

    def limpiar():
        _liberar_recursos()
        for w in vent.winfo_children():
            w.destroy()

    # ---------------- Paso 1: elegir Host / Unirse ----------------
    def paso_elegir():
        limpiar()
        tk.Label(vent, text="Modo Online", font=("Arial", 16, "bold"),
                 fg=TEXTO_CLARO, bg=BG_OSCURO).pack(pady=(28, 6))
        tk.Label(
            vent,
            text=("Necesitás Radmin VPN instalado y conectado\n"
                  "a la misma red virtual que tu rival."),
            font=("Arial", 10), fg=TEXTO_TENUE, bg=BG_OSCURO, justify="center",
        ).pack(pady=(0, 26))

        tk.Button(
            vent, text="SER HOST   (jugás con X)", font=("Arial", 11, "bold"),
            fg="white", bg=VERDE, activebackground="#23897d", activeforeground="white",
            bd=0, pady=12, cursor="hand2", command=paso_host,
        ).pack(fill="x", padx=40, pady=8)

        tk.Button(
            vent, text="UNIRME A UN HOST   (jugás con O)", font=("Arial", 11, "bold"),
            fg="white", bg=AZUL, activebackground="#356485", activeforeground="white",
            bd=0, pady=12, cursor="hand2", command=paso_unirse,
        ).pack(fill="x", padx=40, pady=8)

        tk.Button(
            vent, text="Cancelar", font=("Arial", 9),
            fg=TEXTO_TENUE, bg=BG_OSCURO, activebackground=BG_OSCURO,
            bd=0, cursor="hand2", command=cancelar,
        ).pack(pady=(24, 0))

    # ---------------- Paso Host: esperar conexión ----------------
    def paso_host():
        limpiar()
        conexion = ConexionOnline(es_host=True, puerto=PUERTO_DEFECTO)

        tk.Label(vent, text="Esperando al rival...", font=("Arial", 14, "bold"),
                 fg=TEXTO_CLARO, bg=BG_OSCURO).pack(pady=(26, 10))

        ips = _obtener_ips_locales()
        ips_radmin = [ip for ip in ips if ip.startswith("26.")]
        ips_a_mostrar = ips_radmin if ips_radmin else ips
        texto_ips = "\n".join(ips_a_mostrar) if ips_a_mostrar else "(no se detectó ninguna IP de red)"

        tk.Label(vent, text=("Pasale esta dirección a tu rival\n"
                               "(la de Radmin VPN, suele empezar con 26.):"),
                  font=("Arial", 9), fg=TEXTO_TENUE, bg=BG_OSCURO, justify="center").pack(pady=(0, 6))
        tk.Label(vent, text=texto_ips, font=("Consolas", 13, "bold"),
                 fg=ACENTO, bg=BG_OSCURO, justify="center").pack(pady=(0, 6))
        tk.Label(vent, text=f"Puerto: {PUERTO_DEFECTO}", font=("Arial", 9),
                 fg=TEXTO_TENUE, bg=BG_OSCURO).pack(pady=(0, 4))
        tk.Label(vent, text="(tu partida también se anuncia automáticamente en la red,\n"
                              "así el rival la puede ver en el listado sin escribir la IP)",
                  font=("Arial", 8, "italic"), fg=TEXTO_TENUE, bg=BG_OSCURO,
                  justify="center").pack(pady=(0, 14))

        estado_var = tk.StringVar(value="Escuchando conexiones entrantes...")
        tk.Label(vent, textvariable=estado_var, font=("Arial", 9, "italic"),
                 fg=TEXTO_TENUE, bg=BG_OSCURO, wraplength=380, justify="center").pack(pady=(0, 10))

        # Difunde esta partida por la red (UDP broadcast) para que el
        # paso "Unirme a un Host" la pueda listar automáticamente.
        anunciador = AnunciadorPartida(puerto_juego=PUERTO_DEFECTO)
        anunciador.iniciar()
        recursos_activos.append(anunciador)

        estado = {"listo": False, "ok": False, "cancelado": False}

        def hilo_conectar():
            ok = conexion.conectar()
            estado["ok"] = ok
            estado["listo"] = True

        threading.Thread(target=hilo_conectar, daemon=True).start()

        def revisar():
            if estado["cancelado"]:
                return
            if estado["listo"]:
                anunciador.detener()
                if estado["ok"]:
                    print("[Online] Host: partida iniciada.")
                    resultado["conexion"] = conexion
                    vent.destroy()
                else:
                    estado_var.set(f"Error de conexión: {conexion.error or 'desconocido'}")
                    vent.after(1800, paso_elegir)
                return
            vent.after(200, revisar)

        vent.after(200, revisar)

        def cancelar_host():
            estado["cancelado"] = True
            anunciador.detener()
            conexion.cerrar()
            paso_elegir()

        tk.Button(
            vent, text="Cancelar", font=("Arial", 10, "bold"),
            fg="white", bg=ROJO, activebackground="#c72c39", activeforeground="white",
            bd=0, pady=8, cursor="hand2", command=cancelar_host,
        ).pack(fill="x", padx=60, pady=(8, 0))

    # ---------------- Paso Unirse: elegir partida o pedir IP ----------------
    def paso_unirse():
        limpiar()
        tk.Label(vent, text="Unirme a un Host", font=("Arial", 14, "bold"),
                 fg=TEXTO_CLARO, bg=BG_OSCURO).pack(pady=(20, 10))

        tk.Label(vent, text="Partidas encontradas en la red (Radmin VPN):",
                  font=("Arial", 10, "bold"), fg=TEXTO_CLARO, bg=BG_OSCURO).pack()

        marco_lista = tk.Frame(vent, bg=BG_OSCURO)
        marco_lista.pack(fill="x", padx=40, pady=(6, 2))

        scrollbar = tk.Scrollbar(marco_lista, orient="vertical")
        lista_partidas = tk.Listbox(
            marco_lista, height=5, font=("Consolas", 10),
            bg=BG_TARJETA, fg=TEXTO_CLARO, selectbackground=AZUL,
            selectforeground="white", relief="flat", highlightthickness=0,
            yscrollcommand=scrollbar.set,
        )
        scrollbar.config(command=lista_partidas.yview)
        scrollbar.pack(side="right", fill="y")
        lista_partidas.pack(side="left", fill="both", expand=True, ipady=2)

        partidas_listadas = []  # índice de la lista -> {"ip", "puerto", "nombre"}

        estado_var = tk.StringVar(value="")

        def actualizar_placeholder():
            if not partidas_listadas:
                lista_partidas.delete(0, "end")
                lista_partidas.insert("end", "  Buscando partidas... (nadie anunciado todavía)")
                lista_partidas.itemconfig(0, fg=TEXTO_TENUE)

        actualizar_placeholder()

        buscador = BuscadorPartidas()
        buscador.iniciar()
        recursos_activos.append(buscador)

        def refrescar_lista():
            nuevas = buscador.obtener_encontrados()
            if nuevas:
                if not partidas_listadas:
                    lista_partidas.delete(0, "end")  # sacar el placeholder
                for encontrada in nuevas:
                    clave = (encontrada["ip"], encontrada["puerto"])
                    ya_esta = any((p["ip"], p["puerto"]) == clave for p in partidas_listadas)
                    if not ya_esta:
                        partidas_listadas.append(encontrada)
                        lista_partidas.insert(
                            "end",
                            f"  {encontrada['nombre']}   —   {encontrada['ip']}:{encontrada['puerto']}",
                        )
            if estado.get("vivo", True):
                vent.after(500, refrescar_lista)

        estado = {"vivo": True}
        refrescar_lista()

        def usar_seleccionada(_evento=None):
            seleccion = lista_partidas.curselection()
            if not seleccion or seleccion[0] >= len(partidas_listadas):
                return
            elegida = partidas_listadas[seleccion[0]]
            var_ip.set(elegida["ip"])
            var_puerto.set(str(elegida["puerto"]))
            intentar_conectar()

        lista_partidas.bind("<Double-Button-1>", usar_seleccionada)

        tk.Button(
            vent, text="Unirme a la partida seleccionada", font=("Arial", 10, "bold"),
            fg="white", bg=VERDE, activebackground="#23897d", activeforeground="white",
            bd=0, pady=8, cursor="hand2", command=usar_seleccionada,
        ).pack(fill="x", padx=60, pady=(6, 4))

        tk.Frame(vent, bg="#3a5a80", height=1, width=380).pack(pady=(10, 10))

        tk.Label(vent, text="...o ingresá la IP a mano:", font=("Arial", 9),
                  fg=TEXTO_TENUE, bg=BG_OSCURO).pack()

        var_ip = tk.StringVar()
        entrada_ip = tk.Entry(vent, textvariable=var_ip, font=("Arial", 12), justify="center",
                               bg=BG_TARJETA, fg=TEXTO_CLARO, insertbackground=TEXTO_CLARO,
                               relief="flat")
        entrada_ip.pack(fill="x", padx=60, pady=(4, 8), ipady=6)

        var_puerto = tk.StringVar(value=str(PUERTO_DEFECTO))
        marco_puerto = tk.Frame(vent, bg=BG_OSCURO)
        marco_puerto.pack(pady=(0, 4))
        tk.Label(marco_puerto, text="Puerto:", font=("Arial", 9),
                  fg=TEXTO_TENUE, bg=BG_OSCURO).pack(side="left", padx=(0, 6))
        tk.Entry(marco_puerto, textvariable=var_puerto, font=("Arial", 10), justify="center",
                  width=8, bg=BG_TARJETA, fg=TEXTO_CLARO, insertbackground=TEXTO_CLARO,
                  relief="flat").pack(side="left", ipady=3)

        estado_lbl = tk.Label(vent, textvariable=estado_var, font=("Arial", 9, "italic"),
                               fg=ROJO, bg=BG_OSCURO, wraplength=380, justify="center")
        estado_lbl.pack(pady=(6, 6))

        def intentar_conectar():
            ip = var_ip.get().strip()
            if not ip:
                estado_var.set("Ingresá una dirección IP o elegí una partida del listado.")
                return
            try:
                puerto = int(var_puerto.get().strip())
            except ValueError:
                estado_var.set("El puerto tiene que ser un número.")
                return

            estado["vivo"] = False  # dejamos de refrescar el listado
            buscador.detener()

            btn_conectar.configure(state="disabled", text="Conectando...")
            estado_var.set("Conectando con el host...")

            conexion = ConexionOnline(es_host=False, host=ip, puerto=puerto)
            estado_conexion = {"listo": False, "ok": False}

            def hilo_conectar():
                ok = conexion.conectar()
                estado_conexion["ok"] = ok
                estado_conexion["listo"] = True

            threading.Thread(target=hilo_conectar, daemon=True).start()

            def revisar():
                if estado_conexion["listo"]:
                    if estado_conexion["ok"]:
                        resultado["conexion"] = conexion
                        vent.destroy()
                    else:
                        estado_var.set(
                            f"No se pudo conectar: {conexion.error or 'revisá la IP, el puerto y Radmin VPN'}"
                        )
                        btn_conectar.configure(state="normal", text="Conectar")
                        estado["vivo"] = True
                        buscador.iniciar()
                        refrescar_lista()
                    return
                vent.after(200, revisar)

            vent.after(200, revisar)

        btn_conectar = tk.Button(
            vent, text="Conectar", font=("Arial", 11, "bold"),
            fg="white", bg=VERDE, activebackground="#23897d", activeforeground="white",
            bd=0, pady=8, cursor="hand2", command=intentar_conectar,
        )
        btn_conectar.pack(fill="x", padx=60, pady=(2, 6))

        vent.bind("<Return>", lambda _e: intentar_conectar())

        def volver():
            estado["vivo"] = False
            paso_elegir()

        tk.Button(
            vent, text="Volver", font=("Arial", 9),
            fg=TEXTO_TENUE, bg=BG_OSCURO, activebackground=BG_OSCURO,
            bd=0, cursor="hand2", command=volver,
        ).pack(pady=(2, 0))

    def cancelar():
        _liberar_recursos()
        resultado["conexion"] = None
        vent.destroy()

    vent.protocol("WM_DELETE_WINDOW", cancelar)

    paso_elegir()
    root.wait_window(vent)  # bloquea acá (sin mainloop anidado) hasta que se cierre `vent`

    return resultado["conexion"]


# ======================================================================
# ===========================  interfaz.py  =============================
# ======================================================================
"""
Interfaz gráfica 3D del juego: un cubo fijo (matplotlib 3D) + un
tablerito 2D por capa Z, con controles para orientar el cubo y para
reiniciar la partida.

Toda la interfaz vive dentro de la clase `InterfazJuego`, que recibe un
`Tablero` y, opcionalmente, un `BotIA` cuando el modo de juego es "BOT".
"""


class InterfazJuego:
    """Ventana principal del juego (cubo 3D + tableritos 2D + controles)."""

    ANGULOS_INICIALES = {"X": 20.0, "Y": 0.0, "Z": -60.0}

    def __init__(self, tablero, bot, modo, conexion=None):
        self.tablero = tablero
        self.bot = bot
        self.modo = modo
        self.conexion = conexion  # ConexionOnline, solo si modo == "ONLINE"
        self.mi_jugador = conexion.mi_jugador if conexion is not None else None
        self.tam = tablero.tam

        self.posiciones = [
            (x, y, z)
            for z in range(self.tam) for y in range(self.tam) for x in range(self.tam)
        ]

        # Estado propio de la interfaz (antes eran variables globales)
        self.hover_actual = None
        self.angulos = dict(self.ANGULOS_INICIALES)
        self.eje_activo = "Z"
        self._popup_mostrado = False

        self.rects = {}
        self.textos = {}

        self._construir_figura()
        self._construir_ejes_3d()
        self._construir_tableritos_2d()
        self._construir_controles()
        self._construir_chat()

        self.fig.canvas.mpl_connect("button_press_event", self._on_click)
        self.fig.canvas.mpl_connect("motion_notify_event", self._on_motion)
        self.fig.canvas.mpl_connect("close_event", self._on_close)

        self._actualizar_vista_3d()
        self.dibujar_tablero()

        if self.modo == "ONLINE" and self.conexion is not None:
            self._programar_poll_online()

    # ------------------------------------------------------------------
    # Construcción de la figura y widgets (se corre una sola vez)
    # ------------------------------------------------------------------
    def _construir_figura(self):
        self.fig = plt.figure(figsize=(13.5, 9))
        self.fig.patch.set_facecolor("white")
        self._maximizar_ventana()

        gs = self.fig.add_gridspec(
            2, 3,
            width_ratios=[2.3, 1, 1],
            height_ratios=[1, 1],
            left=0.04, right=0.98, top=0.87, bottom=0.27,
            wspace=0.35, hspace=0.45,
        )

        self.ax = self.fig.add_subplot(gs[:, 0], projection="3d")
        # El cubo ya NO rota al arrastrar con el mouse: la orientación se
        # controla solo con los widgets de eje + ángulo.
        self.ax.disable_mouse_rotation()

        self.ax_layers = [
            self.fig.add_subplot(gs[i // 2, 1 + i % 2]) for i in range(min(self.tam, 4))
        ]
        # Si TAM > 4 no entran todas las capas en la grilla 2x2 de
        # tableritos; se muestran las primeras 4 y el resto solo queda
        # visible en el cubo 3D.
        self.capas_mostradas = list(range(len(self.ax_layers)))

        self.fig.suptitle("", fontsize=16, fontweight="bold")

        modo_desc = MODO_TEXTO.get(self.modo, self.modo)
        self.fig.text(
            0.5, 0.955,
            f"Tablero {self.tam}x{self.tam}x{self.tam} · Modo: {modo_desc}. "
            "Hacé clic en una casilla (tableritos de la derecha, o directo sobre el cubo) para jugar. "
            "El cubo 3D queda fijo: usá 'Girar eje' + el control deslizante para orientarlo.",
            ha="center", va="top", fontsize=9.5, color="#555555",
        )

        leyenda_elementos = [
            Line2D([0], [0], marker="X", color="none", markerfacecolor=COLOR_X,
                   markeredgecolor="black", markersize=11, label="Jugador X"),
            Line2D([0], [0], marker="o", color="none", markerfacecolor=COLOR_O,
                   markeredgecolor="black", markersize=11, label="Jugador O"),
            Line2D([0], [0], marker="s", color="none", markerfacecolor=COLOR_LIBRE,
                   markeredgecolor="none", markersize=11, label="Casilla libre"),
            Line2D([0], [0], marker="s", color="none", markerfacecolor=COLOR_HOVER,
                   markeredgecolor="none", markersize=11, label="Casilla bajo el mouse"),
        ]
        self.fig.legend(handles=leyenda_elementos, loc="lower center", ncol=4,
                         fontsize=9, frameon=False, bbox_to_anchor=(0.5, 0.015))

    def _maximizar_ventana(self):
        """Maximiza la ventana del juego (multiplataforma, backend TkAgg)."""
        try:
            ventana = self.fig.canvas.manager.window
        except Exception:
            return
        try:
            ventana.state("zoomed")  # Windows y algunos Linux/WM
            return
        except Exception:
            pass
        try:
            ventana.attributes("-zoomed", True)  # Linux (varios WM)
            return
        except Exception:
            pass
        try:
            ancho, alto = ventana.maxsize()  # último recurso, multiplataforma
            self.fig.canvas.manager.resize(ancho, alto)
        except Exception:
            pass

    def _construir_ejes_3d(self):
        tam = self.tam
        ax = self.ax

        ax.set_xlim(-0.5, tam - 0.5)
        ax.set_ylim(-0.5, tam - 0.5)
        ax.set_zlim(-0.5, tam - 0.5)
        ax.set_xticks(range(tam))
        ax.set_yticks(range(tam))
        ax.set_zticks(range(tam))

        ax.set_xlabel("X", fontsize=12, fontweight="bold", color=COLOR_EJE_X)
        ax.set_ylabel("Y", fontsize=12, fontweight="bold", color=COLOR_EJE_Y)
        ax.set_zlabel("Z (capa)", fontsize=12, fontweight="bold", color=COLOR_EJE_Z)

        ax.tick_params(axis="x", colors=COLOR_EJE_X)
        ax.tick_params(axis="y", colors=COLOR_EJE_Y)
        ax.tick_params(axis="z", colors=COLOR_EJE_Z)

        ax.xaxis.line.set_color(COLOR_EJE_X)
        ax.yaxis.line.set_color(COLOR_EJE_Y)
        ax.zaxis.line.set_color(COLOR_EJE_Z)

        ax.xaxis.pane.set_edgecolor(COLOR_EJE_X)
        ax.yaxis.pane.set_edgecolor(COLOR_EJE_Y)
        ax.zaxis.pane.set_edgecolor(COLOR_EJE_Z)
        ax.xaxis.pane.set_alpha(0.05)
        ax.yaxis.pane.set_alpha(0.05)
        ax.zaxis.pane.set_alpha(0.05)

        self._dibujar_wireframe_3d()
        self._dibujar_planos_de_capa_3d()

        # Colecciones persistentes en 3D (libres / X / O): mucho más
        # rápido que crear un scatter por casilla.
        self.scat_libres = ax.scatter([], [], [], color=COLOR_LIBRE, s=80, alpha=0.45,
                                       depthshade=False, zorder=1)
        self.scat_x = ax.scatter([], [], [], color=COLOR_X, s=240, marker="X",
                                  depthshade=False, edgecolors="black", linewidths=0.5, zorder=2)
        self.scat_o = ax.scatter([], [], [], color=COLOR_O, s=240, marker="o",
                                  depthshade=False, edgecolors="black", linewidths=0.5, zorder=2)

        # Marcador de "casilla bajo el mouse" en el cubo 3D: un halo
        # dorado sobre la casilla resaltada (misma casilla que en el
        # tablerito 2D correspondiente).
        self.scat_hover_3d = ax.scatter([], [], [], color=COLOR_HOVER, s=420, alpha=0.45,
                                         depthshade=False, zorder=3)

    def _dibujar_wireframe_3d(self):
        """Dibuja solo las 12 aristas del cubo exterior (liviano y rápido)."""
        tam = self.tam
        L = tam - 1
        vertices = [(x, y, z) for x in (0, L) for y in (0, L) for z in (0, L)]
        aristas = []
        for v1 in vertices:
            for v2 in vertices:
                if sum(a != b for a, b in zip(v1, v2)) == 1:
                    aristas.append((v1, v2))
        for (x1, y1, z1), (x2, y2, z2) in aristas:
            self.ax.plot([x1, x2], [y1, y2], [z1, z2], color="#bbbbbb", linewidth=0.8, zorder=0)

    def _dibujar_planos_de_capa_3d(self):
        """Dibuja, dentro del cubo 3D, un cuadrado coloreado en cada capa
        Z (mismo color que el borde/título del tablerito 2D
        correspondiente), para identificar de un vistazo qué capa del
        cubo corresponde a cuál tablerito de la derecha."""
        tam = self.tam
        L = tam - 1
        for z in range(tam):
            color = color_de_capa(z)
            esquinas = [(0, 0, z), (L, 0, z), (L, L, z), (0, L, z), (0, 0, z)]
            xs_, ys_, zs_ = zip(*esquinas)
            self.ax.plot(xs_, ys_, zs_, color=color, linewidth=2.2, alpha=0.9, zorder=1)
            self.ax.text(-0.15, -0.15, z, f"Z{z}", color=color, fontsize=9,
                         fontweight="bold", zorder=4)

    def _construir_tableritos_2d(self):
        """Tableritos 2D (uno por capa Z mostrada). Cada casilla es un
        Rectangle + un texto "X"/"O". Clic 100% preciso: no hace falta
        apuntar en 3D."""
        tam = self.tam

        for idx, axl in enumerate(self.ax_layers):
            z = self.capas_mostradas[idx]
            color_capa = color_de_capa(z)
            axl.set_title(f"Capa Z = {z}", fontsize=11, fontweight="bold", color=color_capa)
            axl.set_xlim(-0.5, tam - 0.5)
            axl.set_ylim(-0.5, tam - 0.5)
            axl.set_aspect("equal")
            axl.set_xticks(range(tam))
            axl.set_yticks(range(tam))
            axl.tick_params(axis="x", colors=COLOR_EJE_X, labelsize=8)
            axl.tick_params(axis="y", colors=COLOR_EJE_Y, labelsize=8)
            for spine in axl.spines.values():
                spine.set_color(color_capa)
                spine.set_linewidth(2.8)

            for y in range(tam):
                for x in range(tam):
                    rect = Rectangle((x - 0.45, y - 0.45), 0.9, 0.9,
                                      facecolor=COLOR_LIBRE, edgecolor="#999999",
                                      linewidth=1.0, alpha=0.6, zorder=1)
                    axl.add_patch(rect)
                    texto = axl.text(x, y, "", ha="center", va="center",
                                      fontsize=13, fontweight="bold", zorder=2)
                    self.rects[(x, y, z)] = rect
                    self.textos[(x, y, z)] = texto

        # Para capas que no tienen tablerito 2D (TAM > 4), igual
        # necesitamos entradas "fantasma" en rects/textos para no romper
        # dibujar_tablero(); como no se dibujan, alcanza con objetos
        # dummy sin agregar al eje.
        for z in range(tam):
            if z in self.capas_mostradas:
                continue
            for y in range(tam):
                for x in range(tam):
                    rect = Rectangle((0, 0), 0, 0)
                    self.rects[(x, y, z)] = rect
                    self.textos[(x, y, z)] = None

    def _construir_controles(self):
        """Controles para orientar el cubo 3D fijo: elegir eje + ángulo.

        Internamente se usa view_init(elev, azim, roll), que es la forma
        que tiene matplotlib de orientar la cámara 3D:
          - "Eje Z" (vertical del tablero) -> azim  (gira el cubo en horizontal)
          - "Eje X"                        -> elev  (inclina el cubo arriba/abajo)
          - "Eje Y"                        -> roll  (rota la vista sobre sí misma)
        """
        fig = self.fig

        fig.text(0.055, 0.235, "Girar eje:", fontsize=10, fontweight="bold", color="#333333")
        ax_radio = fig.add_axes([0.045, 0.135, 0.11, 0.095])
        ax_radio.set_facecolor("#f7f7f7")
        self.radio_eje = RadioButtons(ax_radio, ("X", "Y", "Z"), active=2)
        for etiqueta, color in zip(self.radio_eje.labels, [COLOR_EJE_X, COLOR_EJE_Y, COLOR_EJE_Z]):
            etiqueta.set_color(color)
            etiqueta.set_fontweight("bold")

        ax_slider = fig.add_axes([0.20, 0.17, 0.38, 0.035])
        self.slider_angulo = Slider(ax_slider, "Ángulo", -180.0, 180.0,
                                     valinit=self.angulos[self.eje_activo], valstep=1.0,
                                     color=COLOR_EJE_Z)

        self.radio_eje.on_clicked(self._on_radio_change)
        self.slider_angulo.on_changed(self._on_slider_change)

        ax_btn = fig.add_axes([0.40, 0.065, 0.18, 0.045])
        self.btn_reiniciar = Button(ax_btn, "Reiniciar", color="#f1faee", hovercolor="#a8dadc")
        self.btn_reiniciar.on_clicked(self._on_reset)

    def _construir_chat(self):
        """Panel de chat de texto, flotando abajo a la derecha de la
        ventana (widgets nativos de tkinter superpuestos al canvas de
        matplotlib mediante `place`, así no hay que tocar el layout del
        gridspec). Solo tiene sentido en modo Online, que es el único
        con un rival del otro lado de la red."""
        self.chat_frame = None
        if self.modo != "ONLINE" or self.conexion is None:
            return

        try:
            ventana = self.fig.canvas.manager.window
        except Exception:
            return  # backend sin ventana tkinter: no hay dónde anclar el chat

        try:
            self.chat_frame = tk.Frame(ventana, bg=BG_TARJETA, highlightthickness=1,
                                        highlightbackground=ACENTO)
            self.chat_frame.place(relx=1.0, rely=1.0, anchor="se", x=-16, y=-16,
                                   width=300, height=235)

            tk.Label(self.chat_frame, text="Chat", font=("Arial", 10, "bold"),
                     fg=TEXTO_CLARO, bg=BG_TARJETA).pack(anchor="w", padx=8, pady=(6, 2))

            marco_texto = tk.Frame(self.chat_frame, bg=BG_TARJETA)
            marco_texto.pack(fill="both", expand=True, padx=8)

            scrollbar = tk.Scrollbar(marco_texto, orient="vertical")
            self.chat_texto = tk.Text(
                marco_texto, height=8, font=("Arial", 9), wrap="word",
                bg=BG_OSCURO, fg=TEXTO_CLARO, relief="flat",
                state="disabled", yscrollcommand=scrollbar.set,
            )
            scrollbar.config(command=self.chat_texto.yview)
            scrollbar.pack(side="right", fill="y")
            self.chat_texto.pack(side="left", fill="both", expand=True)

            marco_entrada = tk.Frame(self.chat_frame, bg=BG_TARJETA)
            marco_entrada.pack(fill="x", padx=8, pady=(4, 8))

            self.chat_var = tk.StringVar()
            entrada = tk.Entry(marco_entrada, textvariable=self.chat_var, font=("Arial", 9),
                                bg=BG_OSCURO, fg=TEXTO_CLARO, insertbackground=TEXTO_CLARO,
                                relief="flat")
            entrada.pack(side="left", fill="x", expand=True, ipady=4)
            entrada.bind("<Return>", lambda _e: self._enviar_mensaje_chat())

            tk.Button(
                marco_entrada, text="Enviar", font=("Arial", 9, "bold"),
                fg="white", bg=VERDE, activebackground="#23897d", activeforeground="white",
                bd=0, cursor="hand2", command=self._enviar_mensaje_chat,
            ).pack(side="left", padx=(6, 0))
        except Exception as e:
            print(f"[Chat] No se pudo crear el panel de chat: {e}")
            self.chat_frame = None

    def _agregar_mensaje_chat(self, autor, texto):
        """Agrega una línea al historial del chat (thread-safe respecto a
        matplotlib/tkinter porque siempre se llama desde el hilo
        principal, vía callbacks de eventos o `after`)."""
        if self.chat_frame is None:
            return
        self.chat_texto.configure(state="normal")
        self.chat_texto.insert("end", f"{autor}: {texto}\n")
        self.chat_texto.configure(state="disabled")
        self.chat_texto.see("end")

    def _enviar_mensaje_chat(self):
        if self.chat_frame is None:
            return
        texto = self.chat_var.get().strip()
        if not texto:
            return
        self.chat_var.set("")
        self._agregar_mensaje_chat("Yo", texto)
        if self.conexion is not None:
            self.conexion.enviar_chat(texto)

    # ------------------------------------------------------------------
    # Dibujo del estado del tablero
    # ------------------------------------------------------------------
    def _actualizar_rect_texto(self, x, y, z, val, gana_aqui):
        texto = self.textos[(x, y, z)]
        if texto is None:
            return  # capa sin tablerito 2D visible (TAM > 4)
        rect = self.rects[(x, y, z)]
        if val == 0:
            rect.set_facecolor(COLOR_LIBRE)
            rect.set_alpha(0.6)
            texto.set_text("")
        elif val == -1:
            rect.set_facecolor(COLOR_GANADOR if gana_aqui else "#fddede")
            rect.set_alpha(0.9)
            texto.set_text("X")
            texto.set_color(COLOR_GANADOR if gana_aqui else COLOR_X)
        else:
            rect.set_facecolor(COLOR_GANADOR if gana_aqui else "#dde9f2")
            rect.set_alpha(0.9)
            texto.set_text("O")
            texto.set_color(COLOR_GANADOR if gana_aqui else COLOR_O)

    def dibujar_tablero(self):
        tablero = self.tablero
        libres, xs, os_ = [], [], []
        colores_x, colores_o = [], []

        for (x, y, z) in self.posiciones:
            val = tablero.jugadas[z][y][x]
            es_ultima = (x, y, z) == (tablero.X, tablero.Y, tablero.Z)
            gana_aqui = bool(tablero.g) and es_ultima

            self._actualizar_rect_texto(x, y, z, val, gana_aqui)

            if val == 0:
                libres.append((x, y, z))
            elif val == -1:
                xs.append((x, y, z))
                colores_x.append(COLOR_GANADOR if gana_aqui else COLOR_X)
            else:
                os_.append((x, y, z))
                colores_o.append(COLOR_GANADOR if gana_aqui else COLOR_O)

        def actualizar_3d(scat, puntos, colores=None):
            if puntos:
                xs_, ys_, zs_ = zip(*puntos)
            else:
                xs_, ys_, zs_ = [], [], []
            scat._offsets3d = (xs_, ys_, zs_)
            if colores is not None:
                scat.set_facecolor(colores)

        actualizar_3d(self.scat_libres, libres)
        actualizar_3d(self.scat_x, xs, colores_x)
        actualizar_3d(self.scat_o, os_, colores_o)

        if tablero.g == 1:
            ganador = "X" if tablero.jugadas[tablero.Z][tablero.Y][tablero.X] == -1 else "O"
            self.fig.suptitle(f"¡Gana el jugador {ganador}!", fontsize=16,
                               fontweight="bold", color=COLOR_GANADOR)
        elif tablero.tablero_lleno():
            self.fig.suptitle("¡Empate!", fontsize=16, fontweight="bold", color="#888888")
        else:
            turno = "X" if tablero.jugador == 0 else "O"
            color = COLOR_X if tablero.jugador == 0 else COLOR_O
            if self.modo == "BOT" and tablero.jugador == 1:
                etiqueta_turno = "Turno de la Computadora (O)..."
            elif self.modo == "ONLINE":
                if tablero.jugador == self.mi_jugador:
                    etiqueta_turno = f"Tu turno ({turno})"
                else:
                    etiqueta_turno = f"Turno del rival ({turno})..."
            else:
                etiqueta_turno = f"Turno del jugador: {turno}"
            self.fig.suptitle(etiqueta_turno, fontsize=16, fontweight="bold", color=color)

        self.fig.canvas.draw_idle()

    # ------------------------------------------------------------------
    # Popups de fin de partida
    # ------------------------------------------------------------------
    def _popup(self, titulo, mensaje):
        try:
            ventana = self.fig.canvas.manager.window
        except Exception:
            ventana = None
        try:
            messagebox.showinfo(titulo, mensaje, parent=ventana)
        except Exception:
            messagebox.showinfo(titulo, mensaje)

    def anunciar_resultado_si_corresponde(self):
        """Muestra un popup una sola vez por partida cuando hay ganador o
        empate."""
        tablero = self.tablero
        if self._popup_mostrado:
            return
        if tablero.g == 1:
            ganador = "X" if tablero.jugadas[tablero.Z][tablero.Y][tablero.X] == -1 else "O"
            self._popup_mostrado = True
            self._popup("¡Fin del juego!", f"¡Gana el jugador {ganador}!")
        elif tablero.tablero_lleno():
            self._popup_mostrado = True
            self._popup("¡Fin del juego!", "¡Empate! El tablero se llenó sin ganador.")

    # ------------------------------------------------------------------
    # Detección de casilla bajo el mouse
    # ------------------------------------------------------------------
    def _celda_bajo_mouse_2d(self, event):
        """Determina la casilla (x,y,z) bajo el mouse en un tablerito 2D.
        Es exacto (no hace falta umbral de distancia como en 3D)."""
        if event.inaxes not in self.ax_layers or event.xdata is None or event.ydata is None:
            return None
        z = self.capas_mostradas[self.ax_layers.index(event.inaxes)]
        x = round(event.xdata)
        y = round(event.ydata)
        if 0 <= x < self.tam and 0 <= y < self.tam:
            return (x, y, z)
        return None

    def _celda_mas_cercana_3d(self, event, umbral_px=25):
        """Casilla LIBRE cuya proyección 2D en pantalla está más cerca
        del puntero del mouse sobre el cubo 3D."""
        tablero = self.tablero
        mejor = None
        mejor_dist = None
        for (x, y, z) in self.posiciones:
            if tablero.jugadas[z][y][x] != 0:
                continue
            x2, y2, _ = proj3d.proj_transform(x, y, z, self.ax.get_proj())
            xd, yd = self.ax.transData.transform((x2, y2))
            dist = (xd - event.x) ** 2 + (yd - event.y) ** 2
            if mejor_dist is None or dist < mejor_dist:
                mejor_dist = dist
                mejor = (x, y, z)

        if mejor is not None and mejor_dist is not None and mejor_dist <= umbral_px ** 2:
            return mejor
        return None

    def _fijar_hover(self, celda):
        """Resalta `celda` (o ninguna, si es None) tanto en el tablerito
        2D como en el cubo 3D."""
        if celda == self.hover_actual:
            return

        tablero = self.tablero

        # apagar resaltado anterior en el tablerito 2D
        anterior = self.hover_actual
        if anterior is not None:
            x, y, z = anterior
            if tablero.jugadas[z][y][x] == 0 and self.textos.get((x, y, z)) is not None:
                self.rects[(x, y, z)].set_facecolor(COLOR_LIBRE)
                self.rects[(x, y, z)].set_alpha(0.6)

        self.hover_actual = celda

        # encender resaltado nuevo en el tablerito 2D + halo en el cubo 3D
        if celda is not None:
            x, y, z = celda
            if self.textos.get(celda) is not None:
                self.rects[celda].set_facecolor(COLOR_HOVER)
                self.rects[celda].set_alpha(0.85)
            self.scat_hover_3d._offsets3d = ([x], [y], [z])
        else:
            self.scat_hover_3d._offsets3d = ([], [], [])

        self.fig.canvas.draw_idle()

    # ------------------------------------------------------------------
    # Manejo del turno del bot
    # ------------------------------------------------------------------
    def _bot_juega(self):
        """Ejecuta el turno del bot (si corresponde) y actualiza la vista."""
        tablero = self.tablero
        if not (self.modo == "BOT" and tablero.jugador == 1 and tablero.g == 0):
            return
        casilla = self.bot.movida_bot()
        if casilla is not None:
            tablero.jugar(*casilla)
            self.dibujar_tablero()
            self.anunciar_resultado_si_corresponde()

    def _programar_turno_bot(self):
        """Da un pequeño respiro visual antes de que juegue la compu."""
        tablero = self.tablero
        if not (self.modo == "BOT" and tablero.jugador == 1 and tablero.g == 0):
            return
        try:
            self.fig.canvas.manager.window.after(350, self._bot_juega)
        except Exception:
            self._bot_juega()

    # ------------------------------------------------------------------
    # Callbacks de eventos (mouse, widgets)
    # ------------------------------------------------------------------
    def _on_motion(self, event):
        tablero = self.tablero
        if tablero.g == 1:
            return
        if self.modo == "BOT" and tablero.jugador == 1:
            return  # es el turno de la compu, no resaltar nada
        if self.modo == "ONLINE" and tablero.jugador != self.mi_jugador:
            return  # es el turno del rival, no resaltar nada

        celda = self._celda_bajo_mouse_2d(event)
        if celda is None and event.inaxes == self.ax:
            celda = self._celda_mas_cercana_3d(event)

        self._fijar_hover(celda)

    def _on_click(self, event):
        tablero = self.tablero
        if tablero.g == 1 or event.button != 1:
            return
        if self.modo == "BOT" and tablero.jugador == 1:
            return  # turno de la compu: ignorar clics humanos
        if self.modo == "ONLINE" and tablero.jugador != self.mi_jugador:
            return  # turno del rival: ignorar clics locales

        casilla = self._celda_bajo_mouse_2d(event)
        if casilla is None and event.inaxes == self.ax:
            casilla = self._celda_mas_cercana_3d(event)

        if casilla is not None:
            self._fijar_hover(None)
            if tablero.jugar(*casilla):
                self.dibujar_tablero()
                self.anunciar_resultado_si_corresponde()
                self._programar_turno_bot()
                if self.modo == "ONLINE" and self.conexion is not None:
                    self.conexion.enviar_jugada(*casilla)

    def _actualizar_vista_3d(self):
        self.ax.view_init(elev=self.angulos["X"], azim=self.angulos["Z"], roll=self.angulos["Y"])
        self.fig.canvas.draw_idle()

    def _on_radio_change(self, nuevo_eje):
        self.eje_activo = nuevo_eje
        color_eje = {"X": COLOR_EJE_X, "Y": COLOR_EJE_Y, "Z": COLOR_EJE_Z}[nuevo_eje]
        self.slider_angulo.poly.set_color(color_eje)
        # actualizar la posición del slider sin disparar su propio callback
        self.slider_angulo.eventson = False
        self.slider_angulo.set_val(self.angulos[nuevo_eje])
        self.slider_angulo.eventson = True
        self.fig.canvas.draw_idle()

    def _on_slider_change(self, valor):
        self.angulos[self.eje_activo] = valor
        self._actualizar_vista_3d()

    def _on_reset(self, event):
        self.tablero.reiniciar()
        self._popup_mostrado = False
        self.angulos["X"], self.angulos["Y"], self.angulos["Z"] = (
            self.ANGULOS_INICIALES["X"], self.ANGULOS_INICIALES["Y"], self.ANGULOS_INICIALES["Z"],
        )
        self.eje_activo = "Z"
        self.slider_angulo.eventson = False
        self.slider_angulo.set_val(self.angulos["Z"])
        self.slider_angulo.poly.set_color(COLOR_EJE_Z)
        self.slider_angulo.eventson = True
        try:
            self.radio_eje.set_active(2)
        except Exception:
            pass
        self._actualizar_vista_3d()
        self.dibujar_tablero()

        if self.modo == "ONLINE" and self.conexion is not None:
            self.conexion.enviar_reinicio()

    def _on_close(self, event):
        """Cierra prolijamente la conexión de red (si la hay) al cerrar
        la ventana del juego."""
        if self.conexion is not None:
            self.conexion.cerrar()

    # ------------------------------------------------------------------
    # Modo Online: recepción de mensajes del rival
    # ------------------------------------------------------------------
    def _procesar_mensajes_online(self):
        """Aplica al tablero local los mensajes que llegaron del rival
        desde el último sondeo, y se vuelve a programar a sí misma. Se
        ejecuta siempre en el hilo principal (vía `after`), así que acá
        sí es seguro tocar matplotlib/tkinter."""
        if self.conexion is None:
            return

        tablero = self.tablero
        for mensaje in self.conexion.obtener_mensajes_pendientes():
            tipo = mensaje.get("tipo")

            if tipo == "jugada":
                x, y, z = mensaje.get("x"), mensaje.get("y"), mensaje.get("z")
                if (
                    x is not None and y is not None and z is not None
                    and tablero.g == 0
                    and 0 <= x < tablero.tam and 0 <= y < tablero.tam and 0 <= z < tablero.tam
                    and tablero.jugadas[z][y][x] == 0
                ):
                    tablero.jugar(x, y, z)
                    self.dibujar_tablero()
                    self.anunciar_resultado_si_corresponde()

            elif tipo == "reinicio":
                tablero.reiniciar()
                self._popup_mostrado = False
                self.dibujar_tablero()

            elif tipo == "chat":
                texto = mensaje.get("texto", "")
                if texto:
                    self._agregar_mensaje_chat("Rival", texto)

            elif tipo == "desconectado":
                self._popup(
                    "Conexión perdida",
                    "Se perdió la conexión con el rival "
                    "Es posible que haya abandonado el juego "
                    "puedes seguir jugando localmente o cerrar la ventana.",
                )

        self._programar_poll_online()

    def _programar_poll_online(self):
        """Programa la próxima revisión de mensajes de red (cada
        ~150 ms), sin bloquear el resto de la interfaz."""
        try:
            self.fig.canvas.manager.window.after(150, self._procesar_mensajes_online)
        except Exception:
            pass

    # ------------------------------------------------------------------
    # Punto de entrada
    # ------------------------------------------------------------------
    def iniciar(self):
        """Muestra la ventana y bloquea hasta que el usuario la cierre."""
        plt.show()


# ======================================================================
# =============================  main.py  ===============================
# ======================================================================
"""
Punto de entrada del juego. Se encarga únicamente de "cablear" los
demás componentes:

  1) elegir_configuracion()  -> elige el modo de juego y, si es
                                 Online, deja una ConexionOnline
                                 ya lista (menú tkinter)
  2) Tablero                -> estado y reglas del juego
  3) BotIA                   -> IA del bot (solo si el modo es "BOT")
  4) InterfazJuego            -> ventana matplotlib con el cubo y los
                                 tableritos 2D

Ejecutar con:  python tictactoe3d.py
"""


def main():
    while True:
        config = elegir_configuracion()
        modo = config["modo"]
        if modo is None:
            exit(0)  # el usuario cerró la ventana del menú sin elegir nada

        conexion = config.get("conexion")

        tablero = Tablero(TAM)
        bot = BotIA(tablero) if modo == "BOT" else None

        interfaz = InterfazJuego(tablero, bot, modo, conexion=conexion)
        interfaz.iniciar()


if __name__ == "__main__":
    main()