# -*- coding: utf-8 -*-
"""
main.py
-------
Punto de entrada del juego. Se encarga únicamente de "cablear" los
demás módulos:

  1) menu.elegir_configuracion()  -> elige el modo de juego y, si es
                                       Online, deja una ConexionOnline
                                       ya lista (menú tkinter)
  2) logica.Tablero               -> estado y reglas del juego
  3) bot_ia.BotIA                 -> IA del bot (solo si el modo es "BOT")
  4) interfaz.InterfazJuego       -> ventana matplotlib con el cubo y los
                                       tableritos 2D

Ejecutar con:  python main.py
"""

from config import TAM
from menu import elegir_configuracion
from logica import Tablero
from bot_ia import BotIA
from interfaz import InterfazJuego


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