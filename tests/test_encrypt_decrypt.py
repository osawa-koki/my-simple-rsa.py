
import random
from app.fn_decrypt import decrypt
from app.fn_encrypt import encrypt
from app.fn_getPrivateKey import get_private_key
from app.fn_getPublicKey import get_public_key

primes = [
    11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009,
]
messages = [
    "a",
    "b",
    "c",
    "abc",
    "***",
    "+++",
    "   ",
    "あいうえお",
    "カキクケコ",
    "電子計算機",
]

def test_Encrypt_Decrypt():
    for _ in range(100):
        prime1 = random.choice(primes)
        prime2 = random.choice(primes)
        message = random.choice(messages)

        if prime1 == prime2:
            continue

        # 公開鍵を生成する
        public_key = get_public_key(prime1, prime2)
        if public_key is None:
            raise ValueError(f"public_key is None: prime1: {prime1}, prime2: {prime2}")

        # 秘密鍵を生成する
        private_key = get_private_key(prime1, prime2, public_key)
        if private_key is None:
            raise ValueError(f"private_key is None: prime1: {prime1}, prime2: {prime2}")

        # データを暗号化する
        encrypted = encrypt(public_key, message)

        # 暗号化されたデータを復号する
        decrypted = decrypt(private_key, encrypted)

        assert decrypted == message
