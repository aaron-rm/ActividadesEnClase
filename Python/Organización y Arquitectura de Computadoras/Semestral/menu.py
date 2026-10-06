# -*- coding: utf-8 -*-
"""
menu.py
-------
Pantalla inicial (tkinter) donde el usuario elige el modo de juego:
2 Jugadores, Contra la Computadora, u Online (Host / Unirse por
Radmin VPN).

Expone una única función pública: `elegir_configuracion()`, que abre la
ventana, la espera, y devuelve un dict:
    {"modo": "2P" | "BOT" | "ONLINE", "conexion": ConexionOnline | None}

Si el modo es "ONLINE", "conexion" ya viene conectada y lista para usar
(ver red.py). Si el usuario cancela el sub-flujo de Online, se cae
automáticamente a "2P" con conexion=None.
"""

import socket
import threading

try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    print("Error: tkinter no está instalado. Instalalo con 'pip install tk' o 'sudo apt install python3-tk' (Linux).")

from config import (
    BG_OSCURO, BG_TARJETA, BG_TARJETA_HOVER, ACENTO, VERDE, ROJO, AZUL, TEXTO_CLARO, TEXTO_TENUE,
)
from red import ConexionOnline, PUERTO_DEFECTO, AnunciadorPartida, BuscadorPartidas


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

        # ---- Panel con scroll: puede haber más de una partida abierta,
        # ya que más de una persona puede estar en la misma red virtual. ----
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

        # Escucha los anuncios UDP de cualquier host esperando rival en
        # la red (ver AnunciadorPartida en red.py).
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