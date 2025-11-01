import pytest
from backgammon.core.player import Player

def test_player_bear_off():
    p = Player("Yannick", "white")
    p.bear_off(3)
    assert p.borne_off == 3

def test_player_invalid_color():
    with pytest.raises(ValueError):
        Player("X", "blue")
