from typing import Tuple
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
    block_size = len(str(n)) - 1
    encrypted_blocks = [
        int(encrypted[i:i+block_size+1])
        for i in range(0, len(encrypted), block_size+1)
    ]
    decrypted_chars = [mod_exp(block, d, n) for block in encrypted_blocks]
    decrypted_string = ''.join([chr(char) for char in decrypted_chars])
    decoded_string = bytearray.fromhex(
        ''.join([hex(ord(c))[2:].zfill(2) for c in decrypted_string])
    ).decode('utf-8')
    return decoded_string
