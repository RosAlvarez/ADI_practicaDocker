#!/usr/bin/env python3

"""
    Implementacion ejemplo de servidor y servicio REST
"""
from flask import make_response, request
import json
from restdir.directory import DirectoyException
from restfs_common.constants import ADMIN, ADMIN_TOKEN, USER_TOKEN
from restfs_common.errors import Unauthorized

PERMISSION_ERR = 0
DIR_NOTFOUND_ERR = 1
ALREADYEXISTS_ERR = 2
DOESNOTEXIST_ERR = 3
    

def server(app, directory, AUTH):
    '''Enruta la API REST a la webapp'''

    def _get_effective_user_(req):
        '''Get the user which send the request'''
        try:
            user = AUTH.user_of_token(req.headers.get(USER_TOKEN, None))
            return user
        except Unauthorized:
            if AUTH.is_admin(req.headers.get(ADMIN_TOKEN, None)):
                return ADMIN
        return None

    @app.route("/v1/directory/<dir_id>", methods=["GET"])
    def dir_info(dir_id):
        """Añadir elemento a lista"""
        # headers = request.headers
        # if "admin-token" not in headers and "user-token" not in headers:
        #     return make_response(f"Bad headers", 401)

        # if "admin-token" not in headers:
        #     token = headers["user-token"]
        # else:
        #     token = headers["admin-token"]
        
        user = _get_effective_user_(request)
        if not user:
            return make_response(f"Bad headers", 401)

        try:
            parent, names_childs = directory.get_dir_info(dir_id, user)
            response = {"dir_id": dir_id, "childs": names_childs, "parent": parent}
        except DirectoyException as err:
            if err.code == PERMISSION_ERR:
                return make_response(err.msg, 401)
            if err.code == DIR_NOTFOUND_ERR:
                return make_response(err.msg, 404)

        return make_response(json.dumps(response), 200)

    @app.route("/v1/directory/<dir_id>/<nombre_hijo>", methods=["GET"])
    def dir_childs(dir_id, nombre_hijo):
        """Añadir elemento a lista"""

        # headers = request.headers
        # if "admin-token" not in headers and "user-token" not in headers:
        #     return make_response(f"Bad headers", 401)

        # if "admin-token" not in headers:
        #     token = headers["user-token"]
        # else:
        #     token = headers["admin-token"]

        user = _get_effective_user_(request)
        if not user:
            return make_response(f"Bad headers", 401)

        try:
            childs_list = directory.get_dir_childs(dir_id, nombre_hijo, user)
            response = {"childs_ids": childs_list}
        except DirectoyException as err:
            if err.code == PERMISSION_ERR:
                return make_response(err.msg, 401)
            if err.code == DIR_NOTFOUND_ERR:
                return make_response(err.msg, 404)

        return make_response(json.dumps(response), 200)

    @app.route("/v1/directory/<dir_id>/<nombre_hijo>", methods=["PUT"])
    def new_dir(dir_id, nombre_hijo):
        """Borrar un elemento o la lista entera"""

        # headers = request.headers
        # if "admin-token" not in headers and "user-token" not in headers:
        #     return make_response(f"Bad headers", 401)

        # if "admin-token" not in headers:
        #     token = headers["user-token"]
        # else:
        #     token = headers["admin-token"]
           
        user = _get_effective_user_(request)
        if not user:
            return make_response(f"Bad headers", 401)

        try:
            directory.new_dir(dir_id, nombre_hijo, user)
            id_dir = directory._get_UUID_dir(dir_id, nombre_hijo)
            response = {"dir_id": id_dir}
        except DirectoyException as err:
            if err.code == PERMISSION_ERR:
                return make_response(err.msg, 401)
            if err.code == DIR_NOTFOUND_ERR:
                return make_response(err.msg, 404)
            if err.code == ALREADYEXISTS_ERR:
                return make_response(err.msg, 409)

        return make_response(json.dumps(response), 200)

    @app.route("/v1/directory/<dir_id>/<nombre_hijo>", methods=["DELETE"])
    def remove_dir(dir_id, nombre_hijo):
        '''Obtener el elemento numero "index"'''

        # headers = request.headers
        # if "admin-token" not in headers and "user-token" not in headers:
        #     return make_response(f"Bad headers", 401)

        # if "admin-token" not in headers:
        #     token = headers["user-token"]
        # else:
        #     token = headers["admin-token"]

        user = _get_effective_user_(request)
        if not user:
            return make_response(f"Bad headers", 401)

        try:
            directory.remove_dir(dir_id, nombre_hijo, user)
            response = ""
        except DirectoyException as err:
            if err.code == PERMISSION_ERR:
                return make_response(err.msg, 401)
            if err.code == DIR_NOTFOUND_ERR:
                return make_response(err.msg, 404)
            if err.code == DOESNOTEXIST_ERR:
                return make_response(err.msg, 404)

        return make_response(response, 204)

    @app.route("/v1/files/<dir_id>", methods=["GET"])
    def get_dir_files(dir_id):
        headers = request.headers
        # if "admin-token" not in headers and "user-token" not in headers:
        #     return make_response(f"Bad headers", 401)

        # if "admin-token" not in headers:
        #     token = headers["user-token"]
        # else:
        #     token = headers["admin-token"]

        user = _get_effective_user_(request)
        if not user:
            return make_response(f"Bad headers", 401)

        try:
            names = directory.get_dir_files(dir_id, user)
            response = {"files": names}
        except DirectoyException as err:
            if err.code == PERMISSION_ERR:
                return make_response(err.msg, 401)
            if err.code == DIR_NOTFOUND_ERR:
                return make_response(err.msg, 404)

        return make_response(json.dumps(response), 200)

    @app.route("/v1/files/<dir_id>/<filename>", methods=["GET"])
    def get_file_url(dir_id, filename):
        # headers = request.headers
        # if "admin-token" not in headers and "user-token" not in headers:
        #     return make_response(f"Bad headers", 401)

        # if "admin-token" not in headers:
        #     token = headers["user-token"]
        # else:
        #     token = headers["admin-token"]

        user = _get_effective_user_(request)
        if not user:
            return make_response(f"Bad headers", 401)

        try:
            url = directory.get_file_url(dir_id, filename, user)
        except DirectoyException as err:
            if err.code == PERMISSION_ERR:
                return make_response(err.msg, 401)
            if err.code == DIR_NOTFOUND_ERR:
                return make_response(err.msg, 404)

        return make_response(str(url), 200)

    @app.route("/v1/files/<dir_id>/<filename>", methods=["PUT"])
    def add_file(dir_id, filename):
        url = request.data.decode("utf-8")
        # headers = request.headers
        # if "admin-token" not in headers and "user-token" not in headers:
        #     return make_response(f"Bad headers", 401)

        # if "admin-token" not in headers:
        #     token = headers["user-token"]
        # else:
        #     token = headers["admin-token"]
        
        user = _get_effective_user_(request)
        if not user:
            return make_response(f"Bad headers", 401)

        try:
            url = directory.add_file(dir_id, user, filename, url)
            response = {"URL": url}
            return make_response(json.dumps(response), 200)
        except DirectoyException as err:
            if err.code == PERMISSION_ERR:
                return make_response(err.msg, 401)
            if err.code == DIR_NOTFOUND_ERR:
                return make_response(err.msg, 404)
            if err.code == ALREADYEXISTS_ERR:
                return make_response(err.msg, 400)

    @app.route("/v1/files/<dir_id>/<filename>", methods=["DELETE"])
    def delete_file(dir_id, filename):

        # headers = request.headers
        # if "admin-token" not in headers and "user-token" not in headers:
        #     return make_response(f"Bad headers", 401)

        # if "admin-token" not in headers:
        #     token = headers["user-token"]
        # else:
        #     token = headers["admin-token"]

        user = _get_effective_user_(request)
        if not user:
            return make_response(f"Bad headers", 401)

        try:
            directory.remove_file(dir_id, user, filename)
            return make_response("", 204)
        except DirectoyException as err:
            if err.code == PERMISSION_ERR:
                return make_response(err.msg, 401)
            if err.code == DIR_NOTFOUND_ERR:
                return make_response(err.msg, 404)
            if err.code == DOESNOTEXIST_ERR:
                return make_response(err.msg, 404)
