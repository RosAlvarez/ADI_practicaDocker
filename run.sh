#!/bin/bash

docker volume create dirdb

docker run --name directoryApi -v dirdb:$1 debian-directoryApi

# ./run.sh db/path