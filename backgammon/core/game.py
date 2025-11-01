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
        self.__winner__: str | None = None

    @property
    def turn(self) -> str: return self.__turn__
    @property
    def board(self) -> Board: return self.__board__
    @property
    def moves(self) -> List[int]: return list(self.__moves__)
    def is_finished(self) -> bool: return self.__winner__ is not None
    def winner(self) -> str | None: return self.__winner__

    def roll(self) -> Tuple[int, int, List[int]]:
        if self.is_finished():
            raise InvalidMoveError("La partida ya terminó.")
        d1, d2, values = self.__dice__.roll()
        self.__moves__ = values[:]
        return d1, d2, self.__moves__

    def has_bar(self, color: str) -> bool:
        return self.__board__.bar_count(color) > 0

    def enter_from_bar(self, pip: int) -> None:
        if not self.has_bar(self.__turn__):
            raise InvalidMoveError("No hay fichas en barra para reingresar.")
        if pip not in self.__moves__:
            raise InvalidMoveError("Ese valor no está disponible en la tirada.")
        self.__board__.enter(self.__turn__, pip)
        self.__moves__.remove(pip)
        self._check_turn_end()

    def apply_move(self, src: int, dst: int) -> None:
        if not self.__moves__:
            raise InvalidMoveError("No hay valores de dados disponibles. Tirar con roll() primero.")
        if self.has_bar(self.__turn__):
            raise InvalidMoveError("Debes reingresar desde la barra antes de mover otras fichas.")
        distance = abs(dst - src)
        if distance not in self.__moves__:
            raise InvalidMoveError("El movimiento no coincide con los dados.")
        self.__board__.move(self.__turn__, src, dst)
        self.__moves__.remove(distance)
        self._check_turn_end()

    def bear_off(self, src: int, pip: int) -> None:
        if pip not in self.__moves__:
            raise InvalidMoveError("Ese valor no está disponible en la tirada.")
        self.__board__.bear_off(self.__turn__, src, pip)
        self.__moves__.remove(pip)
        if self.__board__.off_count(self.__turn__) >= 15:
            self.__winner__ = self.__turn__
            self.__moves__.clear()
        else:
            self._check_turn_end()

    def _check_turn_end(self) -> None:
        if not self.__moves__:
            self.__turn__ = "black" if self.__turn__ == "white" else "white"
