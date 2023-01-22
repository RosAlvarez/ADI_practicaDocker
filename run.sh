#!/bin/bash

while getopts u:d:a:l:p: flag
do
    case "${flag}" in
        u) uri_auth=${OPTARG};;
        d) db_path=${OPTARG};;
        a) admin_token=${OPTARG};;
        l) address=${OPTARG};;
        p) port=${OPTARG};;
    esac
done

docker volume create dirdb


docker run --privileged -dti --name dirapi -p 80:${port:-3002} --hostname dirapi -v dirdb:${db_path-'/db'}  debian-dirapi ${uri_auth} ${db_path-'/db'} ${admin_token-'admin'} ${address-'0.0.0.0'} ${port:-3002}

# ./run.sh -u https://auth.serv.com -d /db -a admin -l 0.0.0.0 -p 3002 