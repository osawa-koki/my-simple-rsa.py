from typing import Union
from app.fn_gcd import gcd

def lcm(a: int, b: int) -> Union[int, float]:
    """
    2つの数の最小公倍数を返します。
    :param a: 1つ目の数。
    :param b: 2つ目の数。
    :return: aとbの最小公倍数。
    """
    
    if a == 0 or b == 0:
        return 0
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("引数は整数である必要があります。")
    if a < 0 or b < 0:
        raise ValueError("引数は正の整数である必要があります。")
    return int((a * b) / gcd(a, b))
