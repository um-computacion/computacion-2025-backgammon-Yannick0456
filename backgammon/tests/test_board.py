import pytest
from backgammon.core.board import Board
from backgammon.core.exceptions import InvalidMoveError

def test_standard_setup_counts_and_positions():
    b = Board()
    white = sum(b.point(i).count() for i in range(24) if b.point(i).top_owner() == "white")
    black = sum(b.point(i).count() for i in range(24) if b.point(i).top_owner() == "black")
    assert white == 15
    assert black == 15
    assert b.point(23).count() == 2
    assert b.point(12).count() == 5
    assert b.point(7).count()  == 3
    assert b.point(5).count()  == 5
    assert b.point(0).count()  == 2
    assert b.point(11).count() == 5
    assert b.point(16).count() == 3
    assert b.point(18).count() == 5

def test_simple_hit_sends_checker_to_bar():
    b = Board()
    # Preparamos un destino con 1 ficha negra en idx 11 (ya hay 5 negras en el setup).
    # Mover una blanca desde 12->11 debería golpear y mandar la negra a la barra.
    # Para poder mover, primero colocamos una blanca en 12 que pueda bajar a 11:
    # En el setup ya hay 5 blancas en 12, así que alcanza:
    before = b.bar_count("black")
    b.move("white", 12, 11)
    assert b.bar_count("black") == before + 1

def test_blocked_destination_raises():
    b = Board()
    # idx 11 tiene 5 negras: está bloqueado para blancas (no hay golpe simple).
    with pytest.raises(InvalidMoveError):
        b.move("white", 12, 11)  # acá sí debe fallar si arriba no movimos antes
