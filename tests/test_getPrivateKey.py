import pytest
from app.fn_getPrivateKey import get_private_key

@pytest.mark.parametrize("p, q, publicKey, expectedPrivateKey", [
    (3, 5, (15, 65537), (15, 1)),
    (61, 53, (3233, 17), (3233, 413)),
    (71, 61, (4979, 19), (4979, 199))
])
def test_getPrivateKey(p, q, publicKey, expectedPrivateKey):
    assert get_private_key(p, q, publicKey) == expectedPrivateKey
