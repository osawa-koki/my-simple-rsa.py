
def gcd(a: int, b: int) -> int:
    """
    ユークリッドの互除法を使って、2つの数の最大公約数を返します。

    Args:
        a (int): 1つ目の数。
        b (int): 2つ目の数。

    Returns:
        int: aとbの最大公約数。

    Raises:
        ValueError: 引数が正の整数でない場合に発生します。
    """
    
    if a < 0 or b < 0:
        raise ValueError('引数は正の整数である必要があります。')
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError('引数は正の整数である必要があります。')
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd(b, a % b)
