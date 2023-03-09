from typing import Union, Tuple
from app.fn_gcd import gcd

def getPublicKey(p: int, q: int) -> Union[Tuple[int, int], None]:
    """
    2つの素数を受け取り、公開鍵を返します。

    Args:
        p (int): 素数p
        q (int): 素数q

    Returns:
        Union[Tuple[int, int], None]: 公開鍵 (n, e)。pとqが等しい場合はNoneを返します。

    Raises:
        なし

    Examples:
        >>> get_public_key(17, 19)
        (323, 65537)

        >>> get_public_key(2, 2)
        None
    """
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # The default value for the public exponent.

    if p == q:
        return None

    while gcd(e, phi) != 1:
        e += 1

    return (n, e)
