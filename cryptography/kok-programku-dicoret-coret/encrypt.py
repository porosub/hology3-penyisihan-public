#/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import sys

KEY = "1niL0HkuNc1NY4:)"
IV = b"3Zpz_c8C_r3Cv_IV"


def encrypt(message, passphrase):
    aes = AES.new(passphrase.encode("utf-8"), AES.MODE_CBC, IV)
    return aes.encrypt(pad(message.encode('utf-8'), AES.block_size))


msg = input("enter your message: ")
print(encrypt(msg, KEY).hex())

# hology3{paan_neh_binun_aqu} != flag ya kakaaaaaa
