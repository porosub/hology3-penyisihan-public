#!/usr/bin/env bash

docker kill soal-gunakan
docker rm soal-gunakan
docker run -d --name=soal-gunakan -p 31337:31337/tcp soal-gunakan
