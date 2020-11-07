#!/usr/bin/env python
# python 3.8

import imagehash
import os
from cv2 import imread, imwrite, bitwise_xor
from generator import generator


def encrypt(keypath):
    kunci = imread(keypath)
    harta = imread("harta.png")
    encrypted = bitwise_xor(kunci, harta)
    imwrite("harta_enc.png", encrypted)


def decrypt(keypath):
    kunci = imread(keypath)
    harta_enc = imread("harta_enc.png")
    dec = bitwise_xor(kunci, harta_enc)
    imwrite("harta_dec.png", dec)


def main():
    from PIL import Image
    from Crypto.Util.number import bytes_to_long
    n = 10
    dirname = generator(n)
    fileHashes = list()
    for i in range(n):
        hashFile = imagehash.dhash(Image.open(
            f"{dirname}/key_candidate_{i:02d}.png"), 12)
        fileHashes.append(str(hashFile))

    with open('fileHashes.txt', 'w') as file:
        for fileHash in fileHashes:
            file.write(fileHash+"\n")

    listImage = os.listdir(dirname)
    print(f'banyak image: {len(listImage)}')
    key = os.path.join(
        f"{dirname}/{listImage[bytes_to_long(os.urandom(4)) % 10]}")
    print(key)
    encrypt(key)


if __name__ == '__main__':
    import sys
    status = main()
    sys.exit(status)
