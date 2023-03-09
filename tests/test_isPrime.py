import pytest
from app.fn_isPrime import isPrime

@pytest.mark.parametrize(
    "input, expected_output", [
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (8, False),
        (9, False),
        (10, False),
        (11, True),
        (12, False),
        (13, True),
        (97, True),
        (100, False),
        (113, True),
        (123456789, False),
        (2147483647, True),
    ]
)
def test_is_prime(input, expected_output):
    assert isPrime(input) == expected_output
