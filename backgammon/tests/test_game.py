import pytest
from backgammon.core.game import BackgammonGame
from backgammon.core.exceptions import InvalidMoveError

class FakeDice:
    def __init__(self, seq):
        self.seq = list(seq)
    def roll(self):
        if not self.seq:
            return (1,2,[1,2])
        return self.seq.pop(0)

def test_double_sets_four_moves():
    g = BackgammonGame(dice=FakeDice([(3,3,[3,3,3,3])]))
    d1, d2, values = g.roll()
    assert values == [3,3,3,3]

def test_forced_bar_entry():
    g = BackgammonGame(dice=FakeDice([(1,2,[1,2])]))
    g.board.move("black", 11, 12)
    assert g.board.bar_count("white") == 1
    g.roll()
    with pytest.raises(InvalidMoveError):
        g.apply_move(23, 20)  # debe reingresar primero
    g.enter_from_bar(1)
    assert 1 not in g.moves

def test_bear_off_and_victory_flag():
    g = BackgammonGame(dice=FakeDice([(6,6,[6,6,6,6])]))
    b = g.board
    b.setup_standard()
    # limpiar tablero
    for i in range(24):
        while True:
            try:
                b.point(i).pop()
            except Exception:
                break
    # poner 15 blancas en 0
    from backgammon.core.checker import Checker
    for _ in range(15):
        b.point(0).push(Checker("white"))
    g.roll()
    g.bear_off(0, 6)
    assert b.off_count("white") == 1
