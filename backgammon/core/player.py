class Player:
    """Jugador con nombre, color y conteo de fichas fuera (borne off)."""
    def __init__(self, name: str, color: str) -> None:
        if color not in ("white", "black"):
            raise ValueError("color debe ser 'white' o 'black'")
        self.__name__ = name
        self.__color__ = color
        self.__borne_off__ = 0

    @property
    def name(self) -> str: return self.__name__

    @property
    def color(self) -> str: return self.__color__

    @property
    def borne_off(self) -> int: return self.__borne_off__

    def bear_off(self, count: int = 1) -> None:
        self.__borne_off__ = min(15, self.__borne_off__ + count)
