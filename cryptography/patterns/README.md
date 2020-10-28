# SOAL HOLOGY CRYPTOGRAPHY #2

### Judul : Patterns

### Author : Mr. Grips

## Deskripsi

Di anatara berkas-berkas yang dienkripsi dengan kerahasiaan sempurna ini terdapat flag yang sesungguhnya!

_flag format: <code>/^hology3{[A-z]\*}\$/</code>_

_file: [logs.zip](logs.zip)_

## Konsep Soal

### _Kategori serangan: Known plaintext_

Soal ini mengimplementasikan _One Time Pad_ (OTP) dengan angka yang digenerasikan menggunakan _Linear Congruental Generator_ (LCG) untuk mengenkripsi berkas-berkas yang diberikan. Setiap berkas menggunakan sebuah format penulisan yang kaku dan dienkripsi dengan nilai awal, pengali, serta inkremen yang berbeda yang diberikan pada akhir dari berkas sebelumnya. Akan tetapi, salah satu berkas terenkripsi dengan angka _pseudorandom_ yang polanya sangat terlihat. Hal ini, ditambah dengan penggunaan format penulisan yang sama pada setiap berkas, menimbulkan kelemahan yang dapat dieksploitasi untuk mengetahui isi dari berkas tersebut, yang juga berisi informasi untuk pengenerasian angka _pseudorandom_ untuk berkas berikutnya.

## Proof of Concept

Dapat dilihat pada script yang digunakan untuk menginkripsi bahwa berkas-berkas ini dienkripsi dengan serangkaian key yang dibuat dari 3 buah seed. Soal ini dapat diselesaikan dengan cara melakukan _bruteforce_ operasi XOR antara berkas format dengan berkas berkas yang terenkripsi seperti menggunakan script berikut.

```python
format = open('Format.txt', 'rb').read()
key = bytearray(7)

for i in range(1, 21):
    filename = str(i)
    ciphertext = open(filename, 'rb').read()
    for i1 in range(7):
        key[i1] = format[i1] ^ ciphertext[i1]
    print('---' + str(i) + '---')
    print(key)
```

Meskipun berkas xor memiliki ukuran yang lebih kecil karena masing masing kolom belum diisi, semua berkas (pada saat belum dienkripsi) memiliki kesamaan pada 7 karakter awal; seutas teks yang bertuliskan "Status:" dan hal ini cukup untuk memecahkan enkripsi pada berkas 16.

![Hasil Operasi XOR](https://i.imgur.com/cA273NE.png)

Dapat dilihat bahwa key yang digunakan pada berkas tersebut berawal dari <code>\x02\x05\x0b\x17/\_?</code> angka bernotasi heksadesimal dan karaker-karakter tersebut dengan notasi desimal memiliki nilai: 2, 5, 11, 23, 47, 95, dan 63. Dengan melihat cara key digenerasikan pada [encrypt.py](encrypt.py), dapat disimpulkan bahwa key pada berkas ini berawal dari angka 2, memiliki pengali bernilai 2, inkremen senilai 1, serta modulus sebesar 128. Dengan ini, dapat dihasilkan key yang digunakan untuk mengenkripsi keseluruhan berkasi ini. Setelah melakukan dekripsi dengan cara melakukan operasi XOR anatara key dan berkas yang terenkripsi, dapat ditemukan seed untuk melakukan generasi key yang digunakan pada berkas berikutnya. Setelah melakukan dekripsi hingga berkas 18, dapat ditemukan flag yang sesungguhnya.

## Hints

Apakah dampak dari penggunaan lcg yang tidak tepat?

## Flag

<details>
<summary>Tekan untuk melihat flag</summary>

    hology3{noForm4tOrWe4kMultiples}

</details>
