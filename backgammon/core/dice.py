import random

class Dice:
    """
    Representa dos dados de seis caras para el juego Backgammon.
    """

    def __init__(self):
        self.__last_roll__ = (0, 0)

    def roll(self) -> tuple[int, int]:
        """
        Lanza los dados y devuelve dos valores entre 1 y 6.

        :return: Una tupla con los valores de los dos dados
        """
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        self.__last_roll__ = (d1, d2)
        return self.__last_roll__

    def get_last_roll(self) -> tuple[int, int]:
        """
        Devuelve la última tirada realizada.
        """
        return self.__last_roll__
