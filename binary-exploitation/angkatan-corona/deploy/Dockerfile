FROM ubuntu:bionic
RUN apt-get update
RUN apt-get install -y gcc-multilib nmap
RUN adduser angkatan
COPY libc.so flag.txt soal-ang /home/angkatan/
WORKDIR /home/angkatan/
EXPOSE 31337
USER angkatan
CMD ncat -vc 'LD_PRELOAD=./libc.so ./soal-ang' -kl 0.0.0.0 31337
