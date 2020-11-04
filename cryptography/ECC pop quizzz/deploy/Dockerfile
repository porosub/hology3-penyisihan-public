FROM ubuntu:bionic
RUN apt-get update
RUN apt-get install -y python3 socat python3-pip
RUN adduser ecc
COPY requirements.txt soal-ecc.py /home/ecc/
WORKDIR /home/ecc/
RUN pip3 install -r requirements.txt
EXPOSE 31337
USER ecc
CMD socat -t5 -T30 TCP-LISTEN:31337,reuseaddr,fork EXEC:"python3 soal-ecc.py" > /dev/null 2>&1 