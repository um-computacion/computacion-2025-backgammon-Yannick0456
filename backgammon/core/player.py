class Player:
    """
    Representa un jugador en Backgammon.
    """

    def __init__(self, name: str):
        """
        Inicializa un jugador con un nombre y 15 fichas.

        :param name: Nombre del jugador
        """
        self.__name__ = name
        self.__checkers__ = 15  # cantidad inicial de fichas

    def remove_checker(self):
        """
        Quita una ficha del jugador (ej: al mover al tablero).
        """
        if self.__checkers__ > 0:
            self.__checkers__ -= 1

    def add_checker(self):
        """
        Devuelve una ficha al jugador (ej: al capturar y volver a la barra).
        """
        self.__checkers__ += 1

    def get_name(self) -> str:
        return self.__name__

    def get_checkers(self) -> int:
        return self.__checkers__
