#!/usr/bin/env python
# python 3.8

import random
import numpy as np
import os
import time
from PIL import Image
from Crypto.Util.number import bytes_to_long


def generator(n=100):
    init = int((bytes_to_long("random".encode()) %
                int(time.time() * 100)))
    print(time.time())  # for debugging only
    time.sleep(3.1337)
    random.seed(init)  # for debugging only
    print(init)
    namedir = time.strftime("%Y%m%d%H%M%S")
    os.mkdir(namedir)
    for i in range(n):
        im = Image.new("RGB", (500, 400))
        im = np.array(im)

        for r in range(0, 400):
            for c in range(0, 500):
                re = random.randint(0, 255)
                gr = random.randint(0, 255)
                bl = random.randint(0, 255)
                im[r][c] = [re, gr, bl]
        img = Image.fromarray(im, 'RGB')
        img.save(f"{namedir}/key_candidate_{i:02d}.png")

    return namedir
