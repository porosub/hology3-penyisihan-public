# SOAL HOLOGY CRYPTOGRAPHY #1

### Judul : Kok programku dicoret-coret

### Author : SlimShady

## Deskripsi

Bantu aku untuk mencari IV dari programku ini

_flag format: hology3{IV}_

_file: [corat-coret.png](corat-coret.png)_

## Konsep Soal

### _Kategori serangan: Ciphertext only_

1. Soal ini memacu peserta untuk menggali informasi sedalam"nya dari tiap ciphertext untuk mencari apapun yg dibutuhkan untuk mendapatkan flag
2. Soal ini memacu peserta untuk mencari tahu tentang cara kerja advanced encryption standard

## Proof of Concept

Soal ini terinspirasi dari [sini](https://tildeho.me/ritsec-ctf-writeup-recover-aes-cbc-iv/).

Kurang lebih seperti ini solvernya,

```python
#!/usr/bin/env python2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii
import sys

KEY = "1niL0HkuNc1NY4"
plain2 = "_binun_aqu} != f"
plain3 = "lag ya kakaaaaaa"
plain4 = "aaaaaaaaaaaaaaaa"

cipher1 = "1a00000000000000000000000000006a"
cipher2 = "b22c40003a49dbf8d8e6f49fb141e030"
cipher3 = "b1e4ae96d1ec0d35e515e7bf6d108f8e"
cipher4 = "bc0fb235b00c6f8d4947b13183e09c36"


def decrypt(cipher, passphrase):
    aes = AES.new(passphrase, AES.MODE_CBC, binascii.unhexlify(cipher1))
    return aes.decrypt(cipher)


# iterate through relavent ascii range
def bruteforce(KUNTJI, startChar, endChar):
    KUNTJI = KEY
    for i in range(32, 126):
        for j in range(32, 126):
            key = KUNTJI + chr(i) + chr(j)
            dec_plain2 = decrypt(binascii.unhexlify(cipher2),  key)
            if str(dec_plain2).startswith(startChar) and str(dec_plain2).endswith(endChar):
                KUNTJI = key
                print "The key: ", KUNTJI
                return KUNTJI


KEY = bruteforce(KEY, "_", "f")

def decrypt(cipher, passphrase):
    aes = AES.new(passphrase, AES.MODE_CBC, plain2)
    return aes.decrypt(cipher)


cipher1 = binascii.hexlify(decrypt(binascii.unhexlify(cipher2), KEY))
# # Output result
print "Decrypted data block    : " + cipher1


def decrypt(cipher, passphrase):
    aes = AES.new(passphrase, AES.MODE_CBC, IV)
    return aes.decrypt(cipher)


IV = "hology3{paan_neh"

print "decrypted data (real IV): " + decrypt(binascii.unhexlify(cipher1), KEY)
```

## Hints

<code>None</code>

## Flag

<details>
<summary>Tekan untuk melihat flag</summary>

    hology3{3Zpz_c8C_r3Cv_IV}

</details>
