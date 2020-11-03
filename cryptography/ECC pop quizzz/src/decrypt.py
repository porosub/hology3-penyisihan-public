#!/usr/bin/env python3
from os import urandom
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Membuat Key AES dari shared secret S
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Dekripsi
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext


def encrypt_flag(shared_secret: int, plaintext: bytes):
    # Generate AES key dari shared secret (S)
    iv = urandom(16).hex()
    plaintext = plaintext.hex()
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Enkripsi flag
    plaintext = pad(bytes.fromhex(plaintext), 16)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext)

    return iv, ciphertext.hex()


secretS = None
iv = None
ciphertext = None

print(decrypt_flag(secretS, iv, ciphertext))
