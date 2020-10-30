# SOAL HOLOGY Reverse Engineering #1

### Judul : matematika-sekolah-dasar

### Author : ahm4d

## Deskripsi

Soal latihan matematika untuk sekolah dasar

## Konsep Soal

Mengaitkan masalah soal dengan kehidupan sehari-hari agar mudah dipahami. supaya peserta memahami bagaimana suatu program itu bekerja serta mengetahui algoritmanya.

## Proof of Concept

Karena sebelumnya tadi distrip tidak bisa didebug di gdb jadi program tidak perlu distrip. Untuk mendapatkan flag kita perlu melakukan xor. Kelihatan jelas banget programnya itu mau ngapain. Perlu dicurigai yaitu soal perkalian dan pembagian karena kita harus memasukkan kode. Kode itu sendiri yaitu suatu flag hasil dari xor. Berikut xor dari case 3 (perkalian).
```
 for ( i = 0; i <= 15; ++i )
      {
        if ( (v7[i] ^ dword_4180[i]) == dword_41C0[i] )
          ++v15;
      }
```
Hasil dari xor pada case 3 adalah *COVID19FREELEARNING*

Berikut xor dari case 4 (pembagian)
```
 for ( j = 0; j <= 25; ++j )
      {
        if ( (v7[j] ^ dword_4080[j]) == dword_4100[j] )
          ++v15;
      }
```
Hasil dari xor pada case 4 adalah *hology3{m4teMat1katral414}*

Saya sengaja membuat hampir mirip dari segi variabel atau yang lainnya. Tujuan untuk melihat ketelitian peserta (untuk yang senior CTF mungkin tidak berlaku), serta saya membuat kode berbeda beda, tapi di case 4 (pembagian) adalah flagnya.

## Hints

<code>None</code>

## Flag

<details>
<summary>Tekan untuk melihat flag</summary>

    hology3{m4teMat1katral414}

</details>
