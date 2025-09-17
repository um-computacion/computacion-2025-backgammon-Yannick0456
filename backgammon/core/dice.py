import random
from typing import List, Tuple

class Dice:
    """
    Representa dos dados de seis caras para Backgammon.
    Si sale doble, hay 4 movimientos disponibles.
    """
    def __init__(self, seed: int | None = None):
        self.__rng__ = random.Random(seed)
        self.__last_roll__: Tuple[int, int] = (0, 0)

    def roll(self) -> Tuple[int, int, List[int]]:
        d1 = self.__rng__.randint(1, 6)
        d2 = self.__rng__.randint(1, 6)
        self.__last_roll__ = (d1, d2)
        return d1, d2, ([d1] * 4 if d1 == d2 else [d1, d2])

    def get_last_roll(self) -> Tuple[int, int]:
        return self.__last_roll__
