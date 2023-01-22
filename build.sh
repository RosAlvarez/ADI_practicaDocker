#!/usr/bin/bash

docker build --platform linux/amd64 -f docker/Dockerfile --tag debian-dirapi docker/

docker save debian-dirapi:latest | gzip > debian-dirapi_latest.tar.gz
# ./build.sh