import pytest
from backgammon.core.board import Board
from backgammon.core.exceptions import InvalidMoveError

def test_setup_positions_counts():
    b = Board()
    white = sum(b.point(i).count() for i in range(24) if b.point(i).top_owner() == "white")
    black = sum(b.point(i).count() for i in range(24) if b.point(i).top_owner() == "black")
    assert white == 15 and black == 15
    assert b.point(23).count() == 2
    assert b.point(12).count() == 5
    assert b.point(7).count()  == 3
    assert b.point(5).count()  == 5
    assert b.point(0).count()  == 2
    assert b.point(11).count() == 5
    assert b.point(16).count() == 3
    assert b.point(18).count() == 5

def test_hit_sends_checker_to_bar():
    b = Board()
    before = b.bar_count("black")
    b.move("white", 12, 11)  # golpe en 11
    assert b.bar_count("black") == before + 1

def test_blocked_destination_raises():
    b = Board()
    with pytest.raises(InvalidMoveError):
        b.move("white", 12, 11)

def test_bar_enter_rules():
    b = Board()
    # mandamos una blanca a barra para probar entrada
    b.move("black", 11, 12)  # golpea y manda una blanca de 12 a barra
    assert b.bar_count("white") == 1
    can, idx = b.can_enter("white", 1)
    assert can and idx == 23
