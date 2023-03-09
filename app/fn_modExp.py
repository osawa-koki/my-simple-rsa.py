
def modExp(a: int, b: int, m: int) -> int:
    """
    高速なmod演算を用いてa^b(mod m)を計算します。
    Args:
        a: 底数。
        b: 指数。
        m: 除数。

    Returns:
        a^b (mod m) の結果。
    """

    result = 1
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        b = b // 2
    return result
