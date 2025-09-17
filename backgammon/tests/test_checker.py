import pytest
from backgammon.core.checker import Checker

def test_checker_owner_ok():
    c = Checker("white")
    assert c.owner == "white"

def test_checker_owner_invalid():
    with pytest.raises(ValueError):
        Checker("green")
