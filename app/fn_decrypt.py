import math
from typing import Tuple
import urllib
from app.fn_modExp import mod_exp

def decrypt(private_key: Tuple[int, int], encrypted: str) -> str:
    """秘密鍵を用いて暗号化されたデータを復号します。
    Args:
        private_key (Tuple[int, int]): 復号に使用する秘密鍵。
        encrypted (str): 暗号化されたデータ。
    Returns:
        str: 復号されたデータ。
    """

    n, d = private_key
    block_size = math.floor(math.log10(n) / math.log10(2)) - 1
    encrypted_blocks = [
        block.zfill(block_size + 1)
        for block in [
            encrypted[i:i + block_size + 1]
            for i in range(0, len(encrypted), block_size + 1)
        ]
    ]
    decrypted_chars = [
        mod_exp(int(block), d, n)
        for block in encrypted_blocks
    ]
    decrypted_string = ''.join([
        chr(char)
        for char in decrypted_chars
    ])
    decoded_string = urllib.parse.unquote(decrypted_string)
    return decoded_string
