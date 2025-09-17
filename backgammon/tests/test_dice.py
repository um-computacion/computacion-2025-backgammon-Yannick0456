from backgammon.core.dice import Dice

def test_dice_returns_three_values_and_moves_list():
    d = Dice(seed=42)
    d1, d2, values = d.roll()
    assert isinstance(d1, int) and 1 <= d1 <= 6
    assert isinstance(d2, int) and 1 <= d2 <= 6
    assert isinstance(values, list)

def test_double_produces_four_moves():
    # Probamos varias tiradas hasta encontrar un doble
    d = Dice(seed=1)
    for _ in range(200):
        d1, d2, values = d.roll()
        if d1 == d2:
            assert values == [d1, d1, d1, d1]
            return
    assert False, "No salió doble en 200 tiradas (muy improbable)"

