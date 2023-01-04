FROM debian

ARG AUTH_URI
ARG ADMIN
ARG DB_PATH

## Instalación de paquetes y dependencias
RUN apt-get update && \
    apt-get install -y \
    python3 \
    pip \
    iptables \
    net-tools \
    nano \
    openssh-server \
    sudo && \
    apt-get clean

RUN mkdir -p api_requirements
COPY assets/requirements.txt api_requirements/requirements.txt
RUN pip install api_requirements/requirements.txt


## Copiar Implementación de la API
RUN mkdir -p restdir
ADD src restdir

## Copiar Base de datos
RUN mkdir -p DB_PATH
COPY assets/db/data.db DB_PATH/data.db

## Copiar Script de lanzamiento
RUN mkdir -p restdir_script
COPY script/server_script.py restdir_script/server_script.py

COPY setup.py setup.py

## Lanzamiento entrypoint del docker

# ENV var_uri=${AUTH_URI}
# ENV var_admin=${ADMIN}
# ENV var_dbpath=${DB_PATH}
# ENTRYPOINT [ "entrypoint.sh", var_uri, var_admin, var_dbpath ]

ENTRYPOINT [ "entrypoint.sh" ]




