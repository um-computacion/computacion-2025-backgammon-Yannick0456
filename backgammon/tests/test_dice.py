from backgammon.core.dice import Dice

def test_dice_double_produces_four_moves():
    d = Dice(seed=2)
    found_double = False
    for _ in range(400):
        d1, d2, values = d.roll()
        if d1 == d2:
            assert values == [d1]*4
            found_double = True
            break
    assert found_double

