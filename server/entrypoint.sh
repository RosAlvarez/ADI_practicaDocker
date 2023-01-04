#!/bin/bash
service ssh start

mkdir -p $3
mv /data.db $3/data.db

python3 setup.py install
python3 restdir_script/server_script.py $1 -a $2 -d $3 >/dev/null 2>&1 &


exec /bin/bash