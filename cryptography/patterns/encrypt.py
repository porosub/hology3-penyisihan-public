#!/usr/bin/env python3

fileNum = input('File Number: ')
file = bytearray(open(fileNum + '.txt', 'rb').read())
seed = input('Seed (format is XXX, XXX, XXX): ')
init = int(seed[0:3])
mult = int(seed[5:8])
inc = int(seed[10:13])
key = ""
current = init

for i in range(120):
    key += chr(current)
    current *= mult
    current += inc
    current %= 128

xord_byte = bytearray(120)
byte = bytearray(key, 'ascii')
for i in range(120):
    xord_byte[i] = file[i] ^ byte[i]

open(fileNum, 'wb').write(xord_byte)
