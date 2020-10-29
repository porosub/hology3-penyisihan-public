# Key untuk crack
import random

def random_key (): 
    length = 20
    key = ''
    for i in range(length): 
        key += chr(random.randint(33,65))
    return key

key_count = 20000
out = ''
for i in range(key_count): 
    out += random_key() + '\n'

key_files = open('random5.txt','w')
key_files.write(out)
