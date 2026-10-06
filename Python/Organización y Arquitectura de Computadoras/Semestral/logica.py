# -*- coding: utf-8 -*-
"""
logica.py
---------
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

    # ------------------------------------------------------------------
    # Verificación de líneas ganadoras (usa siempre la ÚLTIMA jugada
    # como referencia: X, Y, Z)
    # ------------------------------------------------------------------
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

    # ------------------------------------------------------------------
    # Acciones sobre el tablero
    # ------------------------------------------------------------------
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
