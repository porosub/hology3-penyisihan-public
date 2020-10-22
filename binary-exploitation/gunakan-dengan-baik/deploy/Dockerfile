FROM ubuntu:bionic
RUN apt-get update
RUN apt-get install -y gcc-multilib ucspi-tcp
RUN adduser gunakan
COPY flag.txt gunakan-dengan-baik /home/gunakan/
WORKDIR /home/gunakan/
EXPOSE 31337
USER gunakan
CMD tcpserver -t 30 -RHl0 0.0.0.0 31337 ./gunakan-dengan-baik
