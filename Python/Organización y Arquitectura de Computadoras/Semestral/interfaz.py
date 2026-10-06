# -*- coding: utf-8 -*-
"""
interfaz.py
-----------
Interfaz gráfica 3D del juego: un cubo fijo (matplotlib 3D) + un
tablerito 2D por capa Z, con controles para orientar el cubo y para
reiniciar la partida.

Toda la interfaz vive dentro de la clase `InterfazJuego`, que recibe un
`Tablero` (logica.py) y, opcionalmente, un `BotIA` (bot_ia.py) cuando el
modo de juego es "BOT". Esto evita el uso de variables globales dispersas
y hace que la ventana se pueda crear/cerrar de forma más prolija.
"""

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

try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    pass

from config import (
    MODO_TEXTO,
    COLOR_X, COLOR_O, COLOR_LIBRE, COLOR_GANADOR, COLOR_HOVER,
    COLOR_EJE_X, COLOR_EJE_Y, COLOR_EJE_Z,
    BG_OSCURO, BG_TARJETA, TEXTO_CLARO, TEXTO_TENUE, ACENTO, VERDE,
    color_de_capa,
)


class InterfazJuego:
    """Ventana principal del juego (cubo 3D + tableritos 2D + controles)."""

    ANGULOS_INICIALES = {"X": 20.0, "Y": 0.0, "Z": -60.0}

    def __init__(self, tablero, bot, modo, conexion=None):
        self.tablero = tablero
        self.bot = bot
        self.modo = modo
        self.conexion = conexion  # red.ConexionOnline, solo si modo == "ONLINE"
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