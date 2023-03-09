import pytest
from app.fn_lcm import lcm

@pytest.mark.parametrize("inputs, expected_output", [
    ([2, 3], 6),
    ([10, 25], 50),
    ([14, 21], 42),
    ([15, 18], 90),
    ([35, 49], 245),
    ([100, 125], 500),
    ([72, 96], 288),
    ([168, 216], 1512),
    ([111, 123], 4551),
    ([222, 123], 9102),
    ([0, 0], 0),
])
def test_lcm(inputs, expected_output):
    assert lcm(*inputs) == expected_output
    assert lcm(inputs[1], inputs[0]) == expected_output

@pytest.mark.parametrize("inputs", [
    [2.5, 3],
    [2, 3.5],
    [-2, 3],
    [2, -3],
])
def test_lcm_error(inputs):
    with pytest.raises(Exception):
        lcm(*inputs)
        lcm(inputs[1], inputs[0])
