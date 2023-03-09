from typing import Tuple
from app.fn_lcm import lcm

def get_private_key(p: int, q: int, public_key: tuple[int, int]) -> tuple[int, int] or None:
    """
    2つの素数p, qと公開鍵public_key(n, e)を受け取り、秘密鍵(n, d)を返します。

    Args:
    p: int - 素数1。
    q: int - 素数2。
    public_key: tuple[int, int] - 公開鍵(n, e)。

    Returns:
    tuple[int, int] or None - 秘密鍵(n, d)。pとqが同じ場合、Noneを返します。
    """

    n, e = public_key
    phi = lcm(p - 1, q - 1)
    d = mod_inv(e, phi)

    if p == q:
        return None

    # dが正の数になるようにする
    while d < 0:
        d += phi

    return n, d

def mod_inv(a: int, m: int) -> int:
    """
    aのmod mにおける逆元を返します。存在しない場合はエラーを返します。

    Args:
    a: int - 逆元を求める数。
    m: int - 剰余の値。

    Returns:
    int - aのmod mにおける逆元。

    Raises:
    Error - 逆元が存在しない場合、エラーを返します。
    """
    gcd_val, x, _ = ext_euclidean(a, m)
    if gcd_val != 1:
        raise ValueError(f'a = {a}(mod {m})における逆元が存在しません。')
    return (x % m + m) % m

def ext_euclidean(a: int, b: int) -> Tuple[int, int, int]:
    """
    拡張ユークリッド互除法。ax + by = gcd(a, b)を満たす[gcd(a, b), x, y]を返す。

    Args:
        a (int): 整数1。
        b (int): 整数2。

    Returns:
        Tuple[int, int, int]: [gcd(a, b), x, y]。ax + by = gcd(a, b)を満たす。

    """
    x, y = 0, 1
    u, v = 1, 0

    while a != 0:
        q = b // a
        r = b % a
        m = x - u * q
        n = y - v * q
        b = a
        a = r
        x = u
        y = v
        u = m
        v = n

    return (b, x, y)
