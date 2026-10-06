# -*- coding: utf-8 -*-
"""
config.py
---------
Constantes y paleta de colores compartidas por todo el proyecto:
tamaño del tablero, textos de los modos de juego y colores usados
tanto en el menú (tkinter) como en la interfaz 3D (matplotlib).

Mantener todo esto en un solo lugar evita "colores mágicos" repetidos
en varios archivos y facilita re-tematizar el juego a futuro.
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

# ------------------------------------------------------------------
# Paleta del MENÚ (tkinter)
# ------------------------------------------------------------------
BG_OSCURO = "#1d3557"
BG_TARJETA = "#274668"
BG_TARJETA_HOVER = "#2f5580"
ACENTO = "#f4a300"
VERDE = "#2a9d8f"
ROJO = "#e63946"
AZUL = "#457b9d"
TEXTO_CLARO = "#f1faee"
TEXTO_TENUE = "#a8dadc"

# ------------------------------------------------------------------
# Paleta del TABLERO / CUBO 3D (matplotlib)
# ------------------------------------------------------------------
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
