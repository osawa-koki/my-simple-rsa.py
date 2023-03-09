
def is_prime(n: int) -> bool:
    """
    受け取った数値が素数かどうかを判定します。

    :param n: 判定する数値
    :type n: int
    :return: 素数ならTrue、そうでなければFalse
    :rtype: bool
    """

    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
