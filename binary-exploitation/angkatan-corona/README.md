# SOAL HOLOGY PWN #2

### Judul : angkatan-corona

### Author : ahm4d

## Deskripsi

Mudah dan bisa hanya berlaku bagi yang rajin

## Konsep Soal

Soal ini merupakan kategori heap exploit memanfaatkan dengan use after free

## Proof of Concept

Inti use after free kita free kan lalu kita modifikasi chunk dengan fungsi memanggil flag.

## Hints

_hint: https://www.youtube.com/watch?v=xzJca3k0tOQ_

## Deployment

```sh
docker build -t soal-angkatan .
bash -c "echo 0 > /proc/sys/kernel/randomize_va_space"

docker run -d --name=soal-angkatan -p 31337:31337/tcp soal-angkatan
crontab /path/to/crontab
```

## Flag

<details>
<summary>Tekan untuk melihat flag</summary>

    hology3{c0ron4CorOnaja9aJ4raK}

</details>
