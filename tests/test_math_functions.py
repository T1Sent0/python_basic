import math
import pytest

"""
    Тест на число PI
"""


def test_pi_value():
    assert abs(math.pi - 3.14159) < 1e-5


def test_pi_precision():
    assert math.pi > 3
    assert math.pi < 4


def test_pi_is_float():
    assert isinstance(math.pi, float)


""""""
"""
    Тест на функцию sqrt
"""


def test_sqrt_positive_numbers():
    assert math.sqrt(4) == 2
    assert math.sqrt(9) == 3
    assert math.sqrt(16) == 4


def test_sqrt_zero():
    assert math.sqrt(0) == 0


def test_sqrt_non_perfect_square():
    assert math.isclose(math.sqrt(2), 1.41421, abs_tol=1e-5)


def test_sqrt_negative_numbers():
    with pytest.raises(ValueError):
        math.sqrt(-1)


def test_sqrt_float_numbers():
    assert math.isclose(math.sqrt(2.25), 1.5, abs_tol=1e-5)


""""""
"""
    Тест на функцию pow
"""


def test_pow_positive_base_positive_exponent():
    assert pow(2, 3) == 8
    assert pow(3, 4) == 81
    assert pow(5, 0) == 1  # Любое число в нулевой степени равно 1


def test_pow_negative_base_positive_exponent():
    assert pow(-2, 3) == -8
    assert pow(-3, 2) == 9


def test_pow_zero_base():
    assert pow(0, 3) == 0
    assert pow(0, 0) == 1  # 0 в нулевой степени равно 1


def test_pow_negative_exponent():
    assert pow(2, -2) == 0.25
    assert pow(5, -1) == 0.2


def test_pow_float_exponent():
    assert pow(4, 0.5) == 2.0  # Квадратный корень
    assert pow(9, 0.5) == 3.0


""""""
"""
    Тест на функцию hypot
"""


def test_hypot_positive_coordinates():
    assert math.hypot(3, 4) == 5.0  # 3-4-5 треугольник
    assert math.hypot(5, 12) == 13.0  # 5-12-13 треугольник


def test_hypot_zero_coordinates():
    assert math.hypot(0, 0) == 0.0  # Гипотенуза нулевого треугольника


def test_hypot_negative_coordinates():
    assert math.hypot(-3, -4) == 5.0  # Гипотенуза с отрицательными координатами
    assert math.hypot(-5, 12) == 13.0  # Также работает с отрицательными x


def test_hypot_float_coordinates():
    assert math.isclose(math.hypot(1.5, 2.5), 2.690, abs_tol=1e-3)


def test_hypot_large_coordinates():
    assert math.hypot(1e6, 1e6) == math.sqrt(2) * 1e6
