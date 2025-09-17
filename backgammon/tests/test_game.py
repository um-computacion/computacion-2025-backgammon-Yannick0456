from __future__ import annotations
from typing import List, Tuple
from .board import Board
from .dice import Dice
from .exceptions import InvalidMoveError


class BackgammonGame:
    """
    Orquesta el flujo del juego (versión simplificada para TP):
    - Mantiene el tablero, el turno, los dados y los valores disponibles
      de la última tirada.
    - Valida que cada movimiento consuma un valor de la tirada.
    - Cambia el turno cuando ya no quedan valores por consumir.
    """

    def __init__(self, dice: Dice | None = None) -> None:
        self.__board__ = Board()
        self.__turn__ = "white"
        self.__dice__ = dice or Dice()
        self.__moves__: List[int] = []

    # --- propiedades de solo lectura ---
    @property
    def turn(self) -> str:
        return self.__turn__

    @property
    def board(self) -> Board:
        return self.__board__

    @property
    def moves(self) -> List[int]:
        """Copia de los valores que quedan por jugar en este turno."""
        return list(self.__moves__)

    # --- acciones del juego ---
    def roll(self) -> Tuple[int, int, List[int]]:
        """
        Tira los dados y registra los valores disponibles para el turno actual.
        Devuelve (d1, d2, values) donde values es [a,b] o [a,a,a,a] si salió doble.
        """
        d1, d2, values = self.__dice__.roll()
        self.__moves__ = values[:]
        return d1, d2, self.__moves__

    def apply_move(self, src: int, dst: int) -> None:
        """
        Aplica un movimiento si coincide con alguno de los valores disponibles.
        - La distancia se calcula como |dst - src| (el sentido se omite en esta versión).
        - Si el destino está bloqueado o el stack es del rival, Board lanzará InvalidMoveError.
        - Tras consumir todos los valores, se alterna el turno.
        """
        if not self.__moves__:
            raise InvalidMoveError("No hay valores de dados disponibles. Tirar con roll() primero.")

        distance = abs(dst - src)
        if distance not in self.__moves__:
            raise InvalidMoveError("El movimiento no coincide con los dados.")

        # mueve en el tablero (valida bloqueos y golpes simples)
        self.__board__.move(self.__turn__, src, dst)

        # consume un valor de la tirada
        self.__moves__.remove(distance)

        # cambio de turno si no quedan más valores
        if not self.__moves__:
            self.__turn__ = "black" if self.__turn__ == "white" else "white"
