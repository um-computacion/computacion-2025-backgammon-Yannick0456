from __future__ import annotations
from typing import List, Optional
from .checker import Checker
from .exceptions import InvalidMoveError

class Point:
    """Un punto del tablero (stack de fichas de un solo color)."""
    def __init__(self) -> None:
        self.__checkers__: List[Checker] = []

    def top_owner(self) -> Optional[str]:
        return self.__checkers__[-1].owner if self.__checkers__ else None

    def count(self) -> int:
        return len(self.__checkers__)

    def push(self, checker: Checker) -> None:
        if self.__checkers__ and self.top_owner() != checker.owner:
            raise InvalidMoveError("No se puede apilar sobre oponente (use golpe).")
        self.__checkers__.append(checker)

    def pop(self) -> Checker:
        if not self.__checkers__:
            raise InvalidMoveError("No hay fichas en el punto.")
        return self.__checkers__.pop()

class Board:
    """Tablero con 24 puntos, barras y setup estándar."""
    def __init__(self) -> None:
        self.__points__ = [Point() for _ in range(24)]
        self.__bar_white__: List[Checker] = []
        self.__bar_black__: List[Checker] = []
        self.setup_standard()

    def setup_standard(self) -> None:
        for p in self.__points__:
            p.__checkers__.clear()
        self.__bar_white__.clear()
        self.__bar_black__.clear()

        def put(i: int, owner: str, n: int) -> None:
            for _ in range(n):
                self.__points__[i].push(Checker(owner))

        # White: 24(2), 13(5), 8(3), 6(5) -> idx 23,12,7,5
        put(23, "white", 2)
        put(12, "white", 5)
        put(7,  "white", 3)
        put(5,  "white", 5)
        # Black: 1(2), 12(5), 17(3), 19(5) -> idx 0,11,16,18
        put(0,  "black", 2)
        put(11, "black", 5)
        put(16, "black", 3)
        put(18, "black", 5)

    def point(self, idx: int) -> Point:
        return self.__points__[idx]

    def move(self, color: str, src: int, dst: int) -> None:
        """Movimiento básico con golpe simple (sin todas las reglas)."""
        piece = self.__points__[src].pop()
        if piece.owner != color:
            raise InvalidMoveError("No puedes mover la ficha del oponente.")
        # golpe simple si hay exactamente 1 del rival
        if self.__points__[dst].count() == 1 and self.__points__[dst].top_owner() != color:
            captured = self.__points__[dst].pop()
            (self.__bar_white__ if captured.owner == "white" else self.__bar_black__).append(captured)
        # destino debe estar vacío o del mismo color
        if self.__points__[dst].top_owner() not in (None, color):
            raise InvalidMoveError("Destino bloqueado.")
        self.__points__[dst].push(piece)

    def bar_count(self, color: str) -> int:
        return len(self.__bar_white__ if color == "white" else self.__bar_black__)
