from __future__ import annotations
from typing import List, Tuple
from .board import Board
from .dice import Dice
from .exceptions import InvalidMoveError


class BackgammonGame:
    def __init__(self, dice: Dice | None = None) -> None:
        self.__board__ = Board()
        self.__turn__ = "white"
        self.__dice__ = dice or Dice()
        self.__moves__: List[int] = []

    @property
    def turn(self) -> str:
        return self.__turn__

    @property
    def board(self) -> Board:
        return self.__board__

    @property
    def moves(self) -> List[int]:
        return list(self.__moves__)

    def roll(self) -> Tuple[int, int, List[int]]:
        d1, d2, values = self.__dice__.roll()
        self.__moves__ = values[:]
        return d1, d2, self.__moves__

    def apply_move(self, src: int, dst: int) -> None:
        if not self.__moves__:
            raise InvalidMoveError("No hay valores de dados disponibles. Tirar primero con roll().")

        distance = abs(dst - src)
        if distance not in self.__moves__:
            raise InvalidMoveError("El movimiento no coincide con los dados.")

        self.__board__.move(self.__turn__, src, dst)
        self.__moves__.remove(distance)

        if not self.__moves__:
            self.__turn__ = "black" if self.__turn__ == "white" else "white"
