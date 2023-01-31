#!/bin/bash
service ssh start

mkdir -p $2
mv /data.db $2/data.db

cd /directory_api && python3 setup.py install
python3 restdir_script/server_script.py $1 -d $2/data.db -a $3 -l $4 -p $5  &

# python3 restdir_script/server_script.py https://auth.serv.com -a admin -d /db


exec /bin/bash