# SOAL HOLOGY CRYPTOGRAPHY #1

### Judul : ECC pop quizzz

### Author : Joule

## Deskripsi

Terinspirasi dari soal RSA quiz di p\\*coctf, Andi yang senang dengan kriptografi membuat soal dengan modifikasi total! Yaitu dengan mengganti menjadi quiz bertemakan ECC. Dapatkah kamu menjawab soal-soal yg disediakan???

## Konsep Soal

### _Kategori serangan: Ciphertext only_

1. Seperti yang tertulis di deskripsi, soal ini terinspirasi dari RSA pop quiz p*coctf 2019. Berisi dasar2 dari konsep _elliptic curve_.

## Proof of Concept

Berikut "kunci jawaban" kuisnya
```text
1. isPrime(p) 
2. 24 -116
3. 169753016558 472169683476
4. 335861726940 159769589376
5. 5630441222594293712 7116794962718930981
6. 1305548989346009163 4148731583499372470
7. 283694777697660492187859152704214518613 136015198097973043243744493947793144040
```
> Untuk yang soal pertama itu hanya perlu diperiksa saja nilai p-nya jika prima maka possible.

Terdapat beberapa tools / library yang daapat memudahkan kita untuk memecahkan soal ini. Akan tetapi minimal kita mengerti dengan operasi yang ada di ECC itu sendiri. Berikut beberapa resource yang pembuat soal rekomendasikan untuk soal ini,
1. Video youtube dari ["Computerphile"](https://www.youtube.com/watch?v=NF1pwjL9-DE) tentang elliptic curve.
2. Video youtube dari ["Trustica"](https://www.youtube.com/watch?v=mFVKuFZ29Fc) tentang elliptic curve.
3. Lecture notes pada [hints](#hints).
4. [Slides](https://informatika.stei.itb.ac.id/~rinaldi.munir/Kriptografi/2014-2015/ECC%20(2015).pdf) dari pak Rinaldi Munir juga dapat membantu.
5. Dokumentasi dari [web trustica](https://trustica.cz/en/2018/03/01/elliptic-curves-over-finite-fields/).
6. [Library](https://github.com/warner/python-ecdsa) python ecdsa
7. [Library](https://github.com/AntonKueltz/fastecdsa) python fastecdsa
8. [Library](https://doc.sagemath.org/html/en/constructions/elliptic_curves.html) sagemath
   
## Hints

Bingung memulai dari mana? Mungkin bisa diperiksa lecture note [berikut](https://crypto.stanford.edu/pbc/notes/elliptic/).

## Flag

<details>
<summary>Tekan untuk melihat flag</summary>

    hology3{nG3rJa1n_s0aL_qU1z_EcC_t1D4kl4h_eZ}

</details>
