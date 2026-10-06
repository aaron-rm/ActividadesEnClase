# -*- coding: utf-8 -*-
"""
bot_ia.py
---------
IA del bot (juega siempre como "O", jugador índice 1, pero el código es
genérico respecto a qué valor le toque). Estrategia:

  1) Si hay una jugada que gana ya, la juega.
  2) Si no, si el rival puede ganar en su próximo turno, bloquea.
  3) Si no, elige la celda con mejor puntaje heurístico (líneas propias
     abiertas + preferencia por el centro), con un poco de azar para no
     ser 100% predecible.

Depende únicamente de un objeto `Tablero` (ver logica.py), al que
consulta y modifica temporalmente para simular jugadas.
"""

import random


def generar_todas_las_lineas(n):
    """Todas las líneas ganadoras posibles (mismas familias que las
    funciones de verificación de logica.Tablero, pero para TODAS las
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
