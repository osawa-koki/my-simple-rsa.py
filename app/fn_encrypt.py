import math
from urllib.parse import quote
from typing import Tuple
from app.fn_modExp import mod_exp

def encrypt(public_key: Tuple[int, int], message: str) -> str:
    """指定された公開鍵でデータを暗号化します。

    Args:
        public_key: 公開鍵 (n, e)。
        message: 暗号化するデータ。

    Returns:
        暗号化されたデータ。

    """

    _message = quote(message)
    n, e = public_key
    block_size = math.floor(math.log10(n) / math.log10(2)) - 1
    blocks = [
        block.zfill(block_size)
        for block in [
            str(ord(char))
            for char in _message
        ]
    ]
    encrypted_blocks = [
        str(mod_exp(int(block), e, n)).zfill(block_size + 1)
        for block in blocks
    ]
    return ''.join(encrypted_blocks)
