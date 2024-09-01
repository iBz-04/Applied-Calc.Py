import pytest
import sympy as sp
from eqn_of_line_calc import \
    linear


def test_linear_basic_case():
    # Test with basic inputs (points (1, 2) and (3, 4))
    result = linear(1, 2, 3, 4)
    expected = 1 * sp.Symbol('x') + 1  # y = x + 1
    assert sp.simplify(result - expected) == 0


def test_linear_horizontal_line():
    # Test with a horizontal line (points (0, 2) and (4, 2))
    result = linear(0, 2, 4, 2)
    expected = 2  # y = 2
    assert sp.simplify(result - expected) == 0


def test_linear_vertical_line():
    # Test with a vertical line (this should raise an exception)
    with pytest.raises(ZeroDivisionError):
        linear(2, 1, 2, 5)


def test_linear_zero_slope():
    # Test with points that should result in zero slope (points (-1, 3) and (2, 3))
    result = linear(-1, 3, 2, 3)
    expected = 3  # y = 3
    assert sp.simplify(result - expected) == 0
