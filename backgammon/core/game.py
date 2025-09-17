from core.board import Board
from core.dice import Dice
from core.player import Player
from core.checker import Checker

class BackgammonGame:
    """
    Coordina el flujo general del juego.
    """
    def __init__(self, jugador1, jugador2):
        self.__board__ = Board()
        self.__dice__ = Dice()
        self.__jugadores__ = [jugador1, jugador2]
        self.__turno__ = 0

    def tirar_dados(self):
        return self.__dice__.tirar()

    def cambiar_turno(self):
        self.__turno__ = 1 - self.__turno__

    def jugador_actual(self):
        return self.__jugadores__[self.__turno__]
