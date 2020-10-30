# SOAL HOLOGY Reverse Engineering #2

### Judul : MK (MOMENT ketika...)

### Author : aldifp01

## Deskripsi

taTUM adalah seorang fisikawan, suatu hari temannya seorang programmer memberikan sebuah source code yang merupakan jalan pengerjaan sebuah soal fisika, tetapi temannya memodifikasi rumus tersebut sehingga pada bagian akhir program tersebut dia menjahili taTUM dengan menambahkan instruksi yang tidak ada pada rumus aslinya, bantulah taTUM menemukan hasil output dari program tersebut

_format flag : hology3{flag}_

_file: [source-code.asm](./src/source-code.asm)_

## Konsep Soal

Konsep soalnya adalah menganalisa cara kerja assembly, untuk soal ini assemblynya adalah compiler intel x86_x64 gcc bukan clang ataupun yang lainnya. untuk cheat sheet atau list syntax yang digunakan dapat dilihat lengkap pada link berikut

- [cs.brown.edu](https://cs.brown.edu/courses/cs033/docs/guides/x64_cheatsheet.pdf)

- [felixcloutier](https://www.felixcloutier.com/x86/cvtsi2sd)

- [mudongliang.github.io](https://mudongliang.github.io/x86/html/file_module_x86_id_58.html)

Soalnya sendiri adalah soal fisika yang ada di contoh soal buku lks intan pariwara kelas 10 semester 2 halaman 80 soal nomor 2 dan semua nilainya ditukar, selain itu pada bagian akhirnya ditambahkan dengan perpangkatan dan percabangan untuk mempersulit sedikit(awalnya rencana soalnya tentang usaha energi tapi terlalu simpel karena hanya perkalian dan pembagian saja, tidak ada menggunakan operator khusus seperti akar dan pangkat).

## Proof of Concept

Untuk penyelesainnya, 3 baris pertama itu tidak termasuk, ketiga baris pertama adalah inisialisasi register yang akan digunakan(??) sehingga dilanjutkan ke 4 baris berikutnya
```
        mov     DWORD PTR [rbp-4], 10
        mov     DWORD PTR [rbp-8], 8
        mov     DWORD PTR [rbp-12], 5875
        mov     DWORD PTR [rbp-16], 19
```
Keempat baris tersebut adalah inisialisasi dari masing masing variabel. Karena bertipe DWORD maka variabel tersebut adalah variabel yang bertipe data bilangan bulat atau integer. Lalu baris berikutnya
```
        mov     eax, DWORD PTR [rbp-4]
        imul    eax, DWORD PTR [rbp-8]
        add     eax, eax
        mov     edi, eax
        call    __gnu_cxx::__enable_if<std::__is_integer<int>::__value, double>::__type std::sqrt<int>(int)
        cvttsd2si       eax, xmm0
        mov     DWORD PTR [rbp-20], eax
```
Kedelapan baris ini adalah satu buah proses dalam bahasa interpreted. ditinjau perbarisnya terlebih dahulu, pertama "mov     eax, DWORD PTR [rbp-4]" berarti kita memasukan nilai rbp-4 ke dalam eax yang dimana **eax sendiri adalah register yang berguna untuk kalkulasi (bisa juga untuk menyimpan nilai sementara)**. lalu pada baris berikutnya register eax dikalikan dengan rbp-8, lanjut baris berikutnya eax ditambah dengan eax itu sendiri sehingga kita memperoleh proses dari 3 baris tersebut dan bisa dijadikan satu sehingga bentuknya kira2 seperti berikut dimisalkan kita buat variabel baru yakni x1 sehingga
```
x1 = rbp-4 * rbp-8
x1 = x1 + x1
x1 = 2 * (rbp-4 * rbp-8) <== diperoleh rumus sehingga
x1 = 2 * (10*8)
x1 = 2 * 80 = 160
```
Pada baris berikutnya nilai eax dimasukan ke dalam register edi, **register edi berfungsi untuk menyimpan/memindahkan lokasi tujuan dari proses yang akan dijalankan**. Lalu pada baris berikutnya terdapat instruksi berikut
```
        call    __gnu_cxx::__enable_if<std::__is_integer<int>::__value, double>::__type std::sqrt<int>(int)
        cvttsd2si       eax, xmm0
```
Baris pertama merupakan instruksi yang berfungsi untuk memanggil fungsi tersebut, sehingga kita buka fungsinya(fungsinya ada setelah main) dan diperoleh source code berikut
```
__gnu_cxx::__enable_if<std::__is_integer<int>::__value, double>::__type std::sqrt<int>(int):
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
        mov     DWORD PTR [rbp-4], edi
        pxor    xmm1, xmm1
        cvtsi2sd        xmm1, DWORD PTR [rbp-4]
        movq    rax, xmm1
        movq    xmm0, rax
        call    sqrt
        movq    rax, xmm0
        movq    xmm0, rax
        leave
        ret
```
Fungsi ini adalah fungsi bawaan yang terdapat pada assembly untuk proses akar atau square root (terbukti dengan adanya pemanggilan operator sqrt) dan akan tetap sama pada program lain apabila memanggil proses ini jadi seperti sudah bawaan pada assembly seperti misalnya println di java kalau dibuka pakai IDE tertentu trus diklik+ctrl nanti muncul bagaimana proses println itu terjadi jadi println sendiri prosesnya tidak dalam 1 baris sama seperti sqrt diatas.

sehingga dari rumus tadi kita bisa melanjutkan prosesnya menjadi berikut
```
x1 = sqrt(x1)
x1 = sqrt(160)
x1 = 12,64911064 <== dibulatkan kebawah karena integer pada assembly membulatkan kebawah sama seperti integer pada c++
x1 = 12

sehingga diperoleh rumus x1 sebagai berikut
x1 = sqrt(2*rbp-4*rbp-8) kita misalkan rbp-4 == a dan rbp-8 == b
x1 = sqrt(2*a*b)
```
Lalu pada baris berikutnya 
```
        mov     eax, DWORD PTR [rbp-4]
        imul    eax, DWORD PTR [rbp-16]
        add     eax, eax
        mov     edi, eax
        call    __gnu_cxx::__enable_if<std::__is_integer<int>::__value, double>::__type std::sqrt<int>(int)
        cvttsd2si       eax, xmm0
        mov     DWORD PTR [rbp-24], eax
```
Kedelapan baris tersebut sama persis seperti 8 baris sebelumnya dan sama2 memanggil fungsi untuk akar kuadrat juga maka pasti rumusnya juga sama yakni x1 = sqrt(2*a*b) bedanya pada yg sekarang bukan dengan rbp-8 tetapi dengan rbp-16 sehingga b pada rumus sebelumnuya bisa saja berupa b1 dan b2 dan a adalah sebuah konstanta karena nilainya tidak berubah sehingga kita peroleh rumus berikut
```
x1 = sqrt(2*a*b1)
x2 = sqrt(2*a*b2)
x2 = sqrt(2*10*19)
x2 = 19
```
Lalu baris berikutnya terdapat instruksi berikut
```
        mov     eax, DWORD PTR [rbp-12]
        imul    eax, DWORD PTR [rbp-20]
        mov     DWORD PTR [rbp-28], eax
        mov     eax, DWORD PTR [rbp-12]
        imul    eax, DWORD PTR [rbp-24]
        mov     DWORD PTR [rbp-32], eax
```
Baris tersebut merupakan instruksi untuk perkalian karena memakai operator imul, dan hanya berbeda pada pengalinya saja (satu menggunakan rbp-20 dan satulagi dengan rbp-24) sehingga bisa dibuat juga seperti x1 dan x2 tadi sehingga
```
rbp-12 = 5875
y1 = rbp-12 * rbp-20
y2 = rbp-12 * rbp-24
rbp-20 dan rbp-24 adalah variabel x1 dan x2 tadi
kita misalkan rbp-12 == c, rbp-20 == d1 dan rbp-24 == d2.
y1 = c * d1
y2 = c * d2
y1 = 5875 * 12 = 70500
y2 = 5875 * 19 = 111625
```
Lalu baris berikutnya terdapat instruksi berikut
```
        mov     eax, DWORD PTR [rbp-36]
        mov     esi, 2
        mov     edi, eax
        call    __gnu_cxx::__promote_2<int, int, __gnu_cxx::__promote<int, std::__is_integer<int>::__value>::__type, __gnu_cxx::__promote<int, std::__is_integer<int>::__value>::__type>::__type std::pow<int, int>(int, int)
        cvttsd2si       eax, xmm0
        mov     DWORD PTR [rbp-36], eax
```
Instruksi tersebut sama seperti operator sqrt jadi dia memanggil fungsi berikut
```
__gnu_cxx::__promote_2<int, int, __gnu_cxx::__promote<int, std::__is_integer<int>::__value>::__type, __gnu_cxx::__promote<int, std::__is_integer<int>::__value>::__type>::__type std::pow<int, int>(int, int):
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
        mov     DWORD PTR [rbp-4], edi
        mov     DWORD PTR [rbp-8], esi
        pxor    xmm0, xmm0
        cvtsi2sd        xmm0, DWORD PTR [rbp-8]
        pxor    xmm2, xmm2
        cvtsi2sd        xmm2, DWORD PTR [rbp-4]
        movq    rax, xmm2
        movapd  xmm1, xmm0
        movq    xmm0, rax
        call    pow
        movq    rax, xmm0
        movq    xmm0, rax
        leave
        ret
```
Fungsi tersebut adalah fungsi untuk pemangkatan (penjelasannya sama kayak di sqrt tadi)
penjelasan lengkap di https://stackoverflow.com/questions/42164550/what-is-happening-here-in-pow-function.

Lalu pada baris berikutnya terdapat instruksi berikut
```
        mov     eax, DWORD PTR [rbp-36]
        cmp     eax, DWORD PTR [rbp-32]
        jle     .L2
```
Instruksi ini adalah instruksi percabangan, jadi nilai rbp-36(pow yang sebelumnya == 1691265625) dimasukan ke register eax lagi, lalu eax dibandingkan dengan rbp-32111625(y2 == 111625) apabila eax lebih kecil(**jle**) maka lompat ke fungsi .l2, apabila tidak maka dilompati instruksi tersebut dan lanjut ke baris seteleahnya, karena 1691265625 lebih besar dari 111625 maka jle dilewati dan lanjut ke baris berikutnya
```
        mov     eax, DWORD PTR [rbp-36]
        or      eax, 19450817
        add     eax, 177013
        mov     DWORD PTR [rbp-36], eax
        jmp     .L3
```
Nilai rbp-36 dimasukan kembali ke eax, lalu di **or** kan (or operasi bitwise bukan or logika) dan ditambahkan sehingga menjadi
```
z =  1691265625 | 19450817 + 177013
z =  1710156761 + 177013
z =  1710333774
```
Untuk rumusnya berasal dari rumus **MOMENTUM 2 benda yang saling bertumbuk** dapat dilihat dari rumus2 sebelumnya
 ```
 xx = sqrt(2*a*bx) sama seperti rumus kecepatan bendanya yakni v = sqrt(2*g*hx)
 yx = c * dx sama seperti rumus momentumnya yakni px = m*vx
 hanya saja instruksi setelahnya bukan rumus momentum ataupun rumus fisika lainnya, hanya perpangkatan biasa dan percabangan agar soalnya lebih panjang sedikit
 ```
maka diperoleh hasil akhir yang merupakan flagnya.


## Hints

<code>None</code>

## Flag

<details>
<summary>Tekan untuk melihat flag</summary>

    hology3{1710333774}

</details>
