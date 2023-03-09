import argparse
from app.fn_getPublicKey import get_public_key
from app.fn_getPrivateKey import get_private_key
from app.fn_encrypt import encrypt
from app.fn_decrypt import decrypt
from app.fn_isPrime import is_prime

parser = argparse.ArgumentParser(description='RSA暗号に基づく暗号化・復号化を行います')
parser.add_argument('--prime1', type=int, required=True, help='素数1')
parser.add_argument('--prime2', type=int, required=True, help='素数2')
parser.add_argument('--message', type=str, required=True, help='メッセージ')
args = parser.parse_args()

print('RSA暗号に基づく暗号化・復号化を行います')

prime1 = args.prime1
prime2 = args.prime2
message = args.message

if not is_prime(prime1):
    raise ValueError('prime1 is not a prime number.')

if not is_prime(prime2):
    raise ValueError('prime2 is not a prime number.')

if prime1 == prime2:
    raise ValueError('prime1 and prime2 must be different.')

# 公開鍵・秘密鍵を生成する
public_key = get_public_key(prime1, prime2)
if public_key is None:
    raise ValueError('public_key is None')
print(f'公開鍵: {public_key}')

private_key = get_private_key(prime1, prime2, public_key)
if private_key is None:
    raise ValueError('private_key is None')
print(f'秘密鍵: {private_key}')

encrypted = encrypt(public_key, message)

# 暗号化されたデータを復号する
decrypted = decrypt(private_key, encrypted)

print(f'元のメッセージ: {message}')
print(f'暗号化されたメッセージ: {encrypted}')
print(f'復号化されたメッセージ: {decrypted}')
