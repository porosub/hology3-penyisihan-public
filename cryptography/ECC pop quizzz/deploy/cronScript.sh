#!/usr/bin/env bash

docker kill soal-ecc
docker rm soal-ecc
docker run -d --name=soal-ecc -p 31337:31337/tcp soal-ecc
