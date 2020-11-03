#!/usr/bin/env python3
import random
import hashlib
from os import urandom
from Crypto.Util.number import isPrime
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES

FLAG = b"hology3{nG3rJa1n_s0aL_qU1z_EcC_t1D4kl4h_eZ}"
a = 9755
b = 1642068

fields = ["Rational", "Finite"]


def posCurve():
    from Crypto.Util.number import bytes_to_long
    branch = bytes_to_long(urandom(4)) % 2
    prime = False
    if (branch == 1):
        ps = [3998648597, 2643504221, 3228135719, 2824378189, 3693441109,
              3034230781, 4053139357, 2940297623, 3565607699, 2716672093]
        p = random.choice(ps)
        prime = isPrime(p)
    else:
        ps = [1187491517, 1417534033, 3182980719, 1793641386, 359527770,
              1549098261, 3425276912, 947052718, 1842803575, 1255778817]
        p = random.choice(ps)
        prime = isPrime(p)
    print(f">>> E: y^2 = x^3 + 9755x + 1642068, p = {p}")
    sys.stdout.flush()
    print(">>> Soal 1. Apakah kurva diatas mungkin untuk digunakan?")
    sys.stdout.flush()
    check = input(">>> [Ya/Tidak]: ")
    check = check.lower()
    if ((check == "ya") and (prime)):
        return True
    elif ((check == "tidak") and (not prime)):
        return True
    return False


def pNegRat():
    P = (24, 116)
    Px = P[0]
    Py = P[1]
    print(f">>> E: y^2 + {a}x + {b}")
    sys.stdout.flush()
    print(f">>> P: ({Px}, {Py})")
    sys.stdout.flush()
    print(">>> Soal 2. Point Negation pada Bidang Rasional (Rational) ")
    sys.stdout.flush()
    print(">>>         dari titik diatas adalah...")
    sys.stdout.flush()
    print(">>> Jawab dengan format 'koordinat x -P<spasi>koordinat y -P'")
    sys.stdout.flush()
    print(">>> Contoh: 100 9")
    sys.stdout.flush()
    checks = input(">>>  (-P) : ")
    checks = checks.split(" ")
    Py_neg = -116
    if ((int(checks[0]) == Px) and (int(checks[1]) == Py_neg)):
        return True
    return False


def pNegFin():
    p, P = (605291795219, (169753016558, 133122111743))
    Px = P[0]
    Py = P[1]
    print(f">>> E: y^2 + {a}x + {b}, p = {p}")
    sys.stdout.flush()
    print(f">>> P: ({Px}, {Py})")
    sys.stdout.flush()
    print(">>> Soal 3. Point Negation pada Bidang Terbatas (Finite) dari ")
    sys.stdout.flush()
    print(">>>         titik diatas adalah...")
    sys.stdout.flush()
    print(">>> Jawab dengan format 'koordinat x -P<spasi>koordinat y -P'")
    sys.stdout.flush()
    print(">>> Contoh: 100 9")
    sys.stdout.flush()
    checks = input(">>>  (-P) : ")
    checks = checks.split(" ")
    Py_neg = 472169683476
    if ((int(checks[0]) == Px) and (int(checks[1]) == Py_neg)):
        return True
    return False


def pAdd():
    p, P, Q = (370776490537, (11357892197, 61229222791, 1),
               (202741803844, 183275925912))
    Px = P[0]
    Py = P[1]
    Qx = Q[0]
    Qy = Q[1]
    print(f">>> E: y^2 + {a}x + 164268, p = {p}")
    sys.stdout.flush()
    print(f">>> P: ({Px}, {Py}) dan Q: ({Qx}, {Qy})")
    sys.stdout.flush()
    print(">>> Soal 4. Point Addition pada Bidang Terbatas (Finite) dari 2 ")
    sys.stdout.flush()
    print(">>>         titik diatas (P + Q) adalah...")
    sys.stdout.flush()
    print(">>> Jawab dengan format 'koordinat x P+Q<spasi>koordinat y P+Q'")
    sys.stdout.flush()
    print(">>> Contoh: 100 9")
    sys.stdout.flush()
    checks = input(">>> (P + Q): ")
    checks = checks.split(" ")
    PQ = (335861726940, 159769589376)
    if ((int(checks[0]) == PQ[0]) and (int(checks[1]) == PQ[1])):
        return True
    return False


def pDoubl():
    p, P = (11014972492788391951, (1257915349831800839, 813189524464815212))
    Px = P[0]
    Py = P[1]
    print(f">>> E: y^2 + {a}x + {b}, p = {p}")
    sys.stdout.flush()
    print(f">>> P: ({Px}, {Py})")
    sys.stdout.flush()
    print(">>> Soal 5. Point Doubling pada Bidang Terbatas (Finite) ")
    sys.stdout.flush()
    print(">>>         dari titik diatas (2P) adalah...")
    sys.stdout.flush()
    print(">>> Jawab dengan format 'koordinat x 2P<spasi>koordinat y 2P'")
    sys.stdout.flush()
    print(">>> Contoh : 100 9")
    sys.stdout.flush()
    checks = input(">>>   (2P) : ")
    checks = checks.split(" ")
    PQ = (5630441222594293712, 7116794962718930981)
    if ((int(checks[0]) == PQ[0]) and (int(checks[1]) == PQ[1])):
        return True
    return False


def scalarMuls():
    p, P = (5706910111343888947, (2743828952426252603, 2509291728312936456))
    Px = P[0]
    Py = P[1]
    print(f">>> E: y^2 + {a}x + {b}, p = {p}")
    sys.stdout.flush()
    print(f">>> P: ({Px}, {Py}), n = 31337")
    sys.stdout.flush()
    print(">>> Soal 6. Nilai Perkalian Titik Skalar dari P diatas (nP)")
    sys.stdout.flush()
    print(">>>         pada Bidang Terbatas (Finite) adalah...")
    sys.stdout.flush()
    print(">>> Jawab dengan format 'koordinat x nP<spasi>koordinat y nP'")
    sys.stdout.flush()
    print(">>> Contoh : 100 9")
    sys.stdout.flush()
    checks = input(">>>   (nP) : ")
    checks = checks.split(" ")
    PQ = (1305548989346009163, 4148731583499372470)
    if ((int(checks[0]) == PQ[0]) and (int(checks[1]) == PQ[1])):
        return True
    return False


def ecdlp():
    p = 291817451140446916363432448685132152963
    G = (51907574400884386828055008599521830361,
         283911536519738385062574093961423903447)
    nA = 61975010211
    nB = 51975080411
    Q_a = (244280649330010236540530914407244752898,
           131840604583564962230200017522074777527)
    print(f">>> E: y^2 + {a}x + {b}, p = {p}")
    sys.stdout.flush()
    print(f">>> G: ({G[0]}, {G[1]})")
    sys.stdout.flush()
    print(f">>> Q_alice: ({Q_a[0]}, {Q_a[1]})")
    sys.stdout.flush()
    print(f">>>  n_bob : ({nB})")
    sys.stdout.flush()
    print(">>> Soal 7. Berapa nilai dari n_bob * Q_alice (S)?")
    sys.stdout.flush()
    print(">>>  *Nilai S merupakan nilai \"shared secret\" yang ")
    sys.stdout.flush()
    print(">>>  akan dipakai oleh alice dan bob untuk komunikasi.")
    sys.stdout.flush()
    print(">>> Jawab dengan format 'koordinat x_S<spasi>koordinat y_S'")
    sys.stdout.flush()
    print(">>> Contoh: 100 9")
    sys.stdout.flush()
    checks = input(">>>   (S) : ")
    checks = checks.split(" ")
    S = (283694777697660492187859152704214518613,
         136015198097973043243744493947793144040)
    iv, ciphertext = encrypt_flag(S[0], FLAG)
    if ((int(checks[0]) == S[0]) and (int(checks[1]) == S[1])):
        print(">>> Congrats, ini hadiah buat kamu:")
        sys.stdout.flush()
        print(f">>> IV = {iv.hex()}, ciphertext = {ciphertext}")
        sys.stdout.flush()
        print(">>> Gunakan shared secret S (koordinat x) ")
        sys.stdout.flush()
        print(">>> untuk decrypt pesan kamu :))))")
        sys.stdout.flush()
        return True
    return False


def encrypt_flag(shared_secret: int, plaintext: bytes):
    # Generate AES key dari digest shared secret (S)
    iv = urandom(16).hex()
    plaintext = plaintext.hex()
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    plaintext = pad(bytes.fromhex(plaintext), 16)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext)

    return iv, ciphertext.hex()


SOAL = {"1": posCurve, "2": pNegRat,
        "3": pNegFin, "4": pAdd,
        "5": pDoubl, "6": scalarMuls,
        "7": ecdlp}


def main():
    try:
        print(">>> =============== ECC POP Quizzz =============== ")
        sys.stdout.flush()
        print(">>> ===> Welcome :) ")
        sys.stdout.flush()
        for function in SOAL:
            print(">>>")
            check = SOAL[function]()
            if (not check):
                raise Exception()
    except:
        print(">>> Waduh ada yang salah kak, jangan diisengin ya :)")


if __name__ == '__main__':
    import sys
    status = main()
    sys.exit(status)
