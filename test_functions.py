from functions import get_max_n, get_phase

SHOTS = 40000


def test_get_max_n():
    n1 = get_max_n(1 / 8, SHOTS)
    assert n1 == 2


def test_get_phase():
    phase = get_phase(1 / 8, SHOTS)
    assert round(phase, 3) == 0.125
