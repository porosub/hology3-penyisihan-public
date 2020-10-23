#!/usr/bin/env bash

docker kill soal-angkatan
docker rm soal-angkatan
docker run -d --name=soal-angkatan -p 31337:31337/tcp soal-angkatan
