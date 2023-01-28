#!/usr/bin/env python3

'''
    Implementacion ejemplo de servidor y servicio REST
'''
import sys
import argparse
import uuid
import os
from flask import Flask
from restfs_dir.directory import Directory
from restfs_dir.server import server
from restfs_dir.auth_client import AuthService
from restfs_common.errors import Unauthorized

def main():
    if len(sys.argv) < 1:
        print("Introducir por lo menos 1 argumento: URL de Auth API")
        sys.exit()

    token = str(uuid.uuid4())
    puerto = 3002
    direccion = "0.0.0.0"
    ruta = os.getcwd()

    parser = argparse.ArgumentParser(description="Restdir arguments")
    parser.add_argument('pos_arg', type=str, help='URL de la API de autenticación') #<- URl api auth
    parser.add_argument("-a", "--admin", action='store', default=token, type=str)
    parser.add_argument("-p", "--port",  action='store', default=puerto, type=int)
    parser.add_argument("-l", "--listening", action='store', default=direccion, type=str)
    parser.add_argument("-d", "--db",  action='store', default=ruta, type=str)

    args = parser.parse_args()

    AUTH=AuthService(args.pos_arg)
    try:
        AUTH.administrator_login(args.admin) #si no es admin salta error
    except Unauthorized as e:
        print(e.__str__)
        sys.exit(1)

    app = Flask("restdir")
    DIR = Directory(args.db, args.admin)
    server(app, DIR,AUTH)
    app.run(host=args.listening, port=args.port, debug=True)


if __name__ == '__main__':
    main()