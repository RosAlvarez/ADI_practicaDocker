#!/bin/bash

docker volume create dirdb

docker run --privileged -dti --name dirapi -p 80:3002 --hostname dirapi -v dirdb:$3 debian-dirapi $1 $2 $3

# ./run.sh https://auth.serv.com admin /db