import tempconv


def test_c_to_f_rounds_to_one_decimal():          # cv-CONV-000001-Tc0nvEx1
    assert tempconv.c_to_f(100) == 212.0
    assert tempconv.c_to_f(36.6) == 97.9


def test_f_to_c_is_the_inverse():                  # cv-CONV-000001-Tc0nvEx1
    assert tempconv.f_to_c(212) == 100.0


def test_below_absolute_zero_is_rejected(capsys):  # cv-CONV-000002-Tc0nvEx1
    assert tempconv.main(["tempconv", "-300C"]) == 2
    assert tempconv.main(["tempconv", "-500F"]) == 2
