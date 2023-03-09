import pytest
from app.fn_modExp import modExp

@pytest.mark.parametrize(
    "inputs, expected_output",
    [
        ([2, 5, 13], 6),
        ([3, 7, 13], 3),
        ([5, 11, 13], 8),
        ([7, 13, 13], 7),
        ([11, 17, 13], 7),
        ([13, 19, 13], 0),
        ([17, 23, 13], 10),
        ([19, 29, 13], 2),
        ([23, 31, 13], 10),
        ([29, 37, 13], 3),
    ],
)
def test_modExp(inputs, expected_output):
    assert modExp(*inputs) == expected_output
