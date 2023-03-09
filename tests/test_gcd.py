
import pytest
from app.fn_gcd import gcd

@pytest.mark.parametrize("x, y, expected_output", [
    (2, 3, 1),
    (10, 25, 5),
    (14, 21, 7),
    (15, 18, 3),
    (35, 49, 7),
    (100, 125, 25),
    (72, 96, 24),
    (168, 216, 24),
    (111, 123, 3),
    (222, 123, 3),
    (0, 0, 0),
    (2, 2, 2),
    (10, 10, 10),
    (0, 10, 10),
    (10, 0, 10),
])
def test_gcd(x, y, expected_output):
    assert gcd(x, y) == expected_output
    assert gcd(y, x) == expected_output

@pytest.mark.parametrize("x, y", [
    (2.5, 3),
    (2, 3.5),
    (-2, 3),
    (2, -3)
])
def test_gcd_with_invalid_input(x, y):
    with pytest.raises(ValueError):
        gcd(x, y)
    with pytest.raises(ValueError):
        gcd(y, x)
