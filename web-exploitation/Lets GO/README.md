# SOAL HOLOGY Web Exploitation #2

### Judul : Lets GO

### Author : Yukazu

## Deskripsi

Lets GO [catch](http://localhost/) em all...

http://localhost/

format flag: `/^hology3{[A-z0-9+_]\\*}$/`

## Konsep Soal

Basic GO route

## Proof of Concept

<!-- TODO -->

## Hints

<code>None</code>

## Deployment

```sh
docker build -t <image-name> .
docker run -d --name=<image-name> -p 8081:8081/tcp <image-name>
```

## Flag

<details>
<summary>Tekan untuk melihat flag</summary>

    hology3{jU5t_a_s1mpl3_G0laNg_r1ddl3}

</details>
