
import pytest
from app.fn_getPublicKey import get_public_key

@pytest.mark.parametrize(
    "p, q, expected",
    [
        (3, 5, (15, 65537)),
        (11, 17, (187, 65537)),
        (101, 103, (10403, 65537)),
        (631, 641, (404471, 65537)),
        (10007, 10009, (100160063, 65537))
    ]
)
def test_get_public_key(p, q, expected):
    assert get_public_key(p, q) == expected
