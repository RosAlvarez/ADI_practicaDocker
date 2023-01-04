#!/usr/bin/bash

docker build -f --platform linux/amd64 server/Dockerfile --tag debian-dirapi server/

# ./build.sh