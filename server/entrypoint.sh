service ssh start

ADMIN = $1

python3 setup.py install
python3 restdir_script/server_script.py -a ADMIN > /dev/null 2>&1
