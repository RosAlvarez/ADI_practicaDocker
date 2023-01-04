service ssh start

AUTH_URI = $AUTH_URI
ADMIN = $ADMIN
DB_PATH = $DB_PATH

python3 setup.py install
python3 restdir_script/server_script.py AUTH_URI -a ADMIN -d DB_PATH &

