from backgammon.core.dice import Dice

def test_roll_returns_two_values():
    d = Dice()
    values = d.roll()
    assert isinstance(values, tuple)
    assert len(values) == 2

def test_roll_values_are_between_1_and_6():
    d = Dice()
    for _ in range(50):  # probar varias veces
        v1, v2 = d.roll()
        assert 1 <= v1 <= 6
        assert 1 <= v2 <= 6

def test_get_last_roll():
    d = Dice()
    rolled = d.roll()
    assert d.get_last_roll() == rolled
