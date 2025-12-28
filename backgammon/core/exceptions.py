class RuleError(Exception):
    """Regla inválida o no soportada."""

class InvalidMoveError(RuleError):
    """Movimiento inválido en el contexto actual."""
