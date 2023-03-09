from typing import Tuple

def encrypt(public_key: Tuple[int, int], message: str) -> str:
    """指定された公開鍵でデータを暗号化します。

    Args:
        public_key: 公開鍵 (n, e)。
        message: 暗号化するデータ。

    Returns:
        暗号化されたデータ。

    """

    _message = message.encode('utf-8').hex()
    n, e = public_key
    block_size = n.bit_length() // 8 - 1
    blocks = [int(_message[i:i+block_size], 16) for i in range(0, len(_message), block_size)]
    encrypted_blocks = [str(pow(num, e, n)).zfill(block_size+1) for num in blocks]
    return ''.join(encrypted_blocks)
