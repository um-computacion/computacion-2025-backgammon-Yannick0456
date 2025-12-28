class Checker:
    """Ficha de backgammon: pertenece a un color (white/black)."""
    def __init__(self, owner: str) -> None:
        if owner not in ("white", "black"):
            raise ValueError("owner debe ser 'white' o 'black'")
        self.__owner__ = owner

    @property
    def owner(self) -> str:
        return self.__owner__
