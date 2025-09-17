import pytest
from backgammon.core.player import Player

def test_player_properties_and_bear_off():
    p = Player("Yannick", "white")
    assert p.name == "Yannick"
    assert p.color == "white"
    assert p.borne_off == 0
    p.bear_off(3)
    assert p.borne_off == 3

def test_player_invalid_color_raises():
    with pytest.raises(ValueError):
        Player("X", "blue")
