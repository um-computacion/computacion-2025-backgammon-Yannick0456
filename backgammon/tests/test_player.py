import pytest
from backgammon.core.player import Player

def test_player_initial_state():
    p = Player("Franco")
    assert p.get_name() == "Franco"
    assert p.get_checkers() == 15

def test_remove_checker():
    p = Player("Franco")
    p.remove_checker()
    assert p.get_checkers() == 14

def test_add_checker():
    p = Player("Franco")
    p.add_checker()
    assert p.get_checkers() == 16

def test_cannot_go_negative():
    p = Player("Franco")
    for _ in range(20):  # intenta quitar más de lo posible
        p.remove_checker()
    assert p.get_checkers() >= 0
