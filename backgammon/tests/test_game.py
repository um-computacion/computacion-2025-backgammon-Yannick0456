import pytest
from backgammon.core.game import BackgammonGame

class FakeDice:
    """Dado determinista para pruebas."""
    def __init__(self, d1: int, d2: int):
        self.d1, self.d2 = d1, d2
    def roll(self):
        return (self.d1, self.d2, [self.d1]*4) if self.d1 == self.d2 else (self.d1, self.d2, [self.d1, self.d2])

def test_roll_with_double_sets_four_moves():
    g = BackgammonGame(dice=FakeDice(2, 2))
    d1, d2, values = g.roll()
    assert (d1, d2) == (2, 2)
    assert values == [2, 2, 2, 2]
    assert g.moves == [2, 2, 2, 2]

def test_apply_move_consumes_and_switches_turn():
    g = BackgammonGame(dice=FakeDice(3, 5))
    g.roll()
    assert g.turn == "white"
    g.apply_move(23, 20)  # usa 3
    assert g.moves == [5]
    g.apply_move(12, 7)   # usa 5
    assert g.turn == "black"
    assert g.moves == []

def test_apply_move_without_roll_raises():
    g = BackgammonGame(dice=FakeDice(1, 2))
    with pytest.raises(Exception):
        g.apply_move(23, 22)

def test_apply_move_with_wrong_distance_raises():
    g = BackgammonGame(dice=FakeDice(4, 4))
    g.roll()
    with pytest.raises(Exception):
        g.apply_move(23, 22)
