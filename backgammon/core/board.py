from __future__ import annotations
from typing import List, Optional, Tuple
from .checker import Checker
from .exceptions import InvalidMoveError

class Point:
    def __init__(self) -> None:
        self.__checkers__: List[Checker] = []

    def top_owner(self) -> Optional[str]:
        return self.__checkers__[-1].owner if self.__checkers__ else None

    def count(self) -> int:
        return len(self.__checkers__)

    def push(self, checker: Checker) -> None:
        if self.__checkers__ and self.top_owner() != checker.owner:
            raise InvalidMoveError("No se puede apilar sobre oponente (use golpe)." )
        self.__checkers__.append(checker)

    def pop(self) -> Checker:
        if not self.__checkers__:
            raise InvalidMoveError("No hay fichas en el punto.")
        return self.__checkers__.pop()

class Board:
    def __init__(self) -> None:
        self.__points__ = [Point() for _ in range(24)]
        self.__bar_white__: List[Checker] = []
        self.__bar_black__: List[Checker] = []
        self.__off_white__: List[Checker] = []
        self.__off_black__: List[Checker] = []
        self.setup_standard()

    def setup_standard(self) -> None:
        for p in self.__points__:
            p.__checkers__.clear()
        self.__bar_white__.clear(); self.__bar_black__.clear()
        self.__off_white__.clear(); self.__off_black__.clear()

        def put(i: int, owner: str, n: int) -> None:
            for _ in range(n):
                self.__points__[i].push(Checker(owner))

        put(23, "white", 2); put(12, "white", 5); put(7, "white", 3); put(5, "white", 5)
        put(0,  "black", 2); put(11, "black", 5); put(16, "black", 3); put(18, "black", 5)

    def point(self, idx: int) -> Point: return self.__points__[idx]

    def bar_count(self, color: str) -> int:
        return len(self.__bar_white__ if color == "white" else self.__bar_black__)

    def off_count(self, color: str) -> int:
        return len(self.__off_white__ if color == "white" else self.__off_black__)

    def is_blocked(self, color: str, idx: int) -> bool:
        top = self.__points__[idx].top_owner()
        cnt = self.__points__[idx].count()
        return top not in (None, color) and cnt >= 2

    def move(self, color: str, src: int, dst: int) -> None:
        piece = self.__points__[src].pop()
        if piece.owner != color:
            raise InvalidMoveError("No puedes mover la ficha del oponente.")
        if self.__points__[dst].count() == 1 and self.__points__[dst].top_owner() != color:
            captured = self.__points__[dst].pop()
            (self.__bar_white__ if captured.owner == "white" else self.__bar_black__).append(captured)
        if self.is_blocked(color, dst):
            raise InvalidMoveError("Destino bloqueado.")
        self.__points__[dst].push(piece)

    def can_enter(self, color: str, pip: int) -> Tuple[bool, int]:
        if pip < 1 or pip > 6:
            return (False, -1)
        idx = 24 - pip if color == "white" else pip - 1
        return (not self.is_blocked(color, idx), idx)

    def enter(self, color: str, pip: int) -> None:
        can, idx = self.can_enter(color, pip)
        if not can:
            raise InvalidMoveError("No puede entrar desde barra con ese valor (bloqueado)." )
        bar = self.__bar_white__ if color == "white" else self.__bar_black__
        if not bar:
            raise InvalidMoveError("No hay fichas en la barra para reingresar.")
        piece = bar.pop()
        if self.__points__[idx].count() == 1 and self.__points__[idx].top_owner() != color:
            captured = self.__points__[idx].pop()
            (self.__bar_white__ if captured.owner == "white" else self.__bar_black__).append(captured)
        if self.is_blocked(color, idx):
            raise InvalidMoveError("Destino de entrada bloqueado.")
        self.__points__[idx].push(piece)

    def in_home_board(self, color: str) -> bool:
        rng = range(0, 6) if color == "white" else range(18, 24)
        total_on_board = 0
        for i in range(24):
            if self.__points__[i].top_owner() == color:
                total_on_board += self.__points__[i].count()
        home = sum(self.__points__[i].count() for i in rng if self.__points__[i].top_owner() == color)
        bar = self.bar_count(color)
        off = self.off_count(color)
        return (bar == 0) and (home + off == total_on_board + off)

    def bear_off(self, color: str, src: int, pip: int) -> None:
        if not self.in_home_board(color):
            raise InvalidMoveError("No se puede hacer bear-off si no están todas en el home.")
        distance = (src + 1) if color == "white" else (24 - src)
        if pip == distance:
            piece = self.__points__[src].pop()
            (self.__off_white__ if color == "white" else self.__off_black__).append(piece)
            return
        if pip > distance:
            more_far_exists = False
            if color == "white":
                for i in range(src+1, 6):
                    if self.__points__[i].top_owner() == "white" and self.__points__[i].count() > 0:
                        more_far_exists = True; break
            else:
                for i in range(18, src):
                    if self.__points__[i].top_owner() == "black" and self.__points__[i].count() > 0:
                        more_far_exists = True; break
            if not more_far_exists:
                piece = self.__points__[src].pop()
                (self.__off_white__ if color == "white" else self.__off_black__).append(piece)
                return
        raise InvalidMoveError("No se puede hacer bear-off con ese valor desde esa posición.")