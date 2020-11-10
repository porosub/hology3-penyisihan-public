FROM golang:1.15-buster

WORKDIR /app
COPY . .
RUN go get ./... 
RUN go build 

EXPOSE 14022
CMD [ "go", "run", "server.go" ]