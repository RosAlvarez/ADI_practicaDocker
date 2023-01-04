#!/usr/bin/bash

#su root -c "docker build -f server/Dockerfile --tag debian-directoryApi --build-arg AUTH_URI=URI --build-arg ADMIN=TOKEN --build-arg DB_PATH=PATH"

docker build -f server/Dockerfile --tag debian-dirapi --build-arg AUTH_URI=$1,ADMIN=$2,DB_PATH=$3 server/

# ./build.sh https://auth.serv.com admin db/path