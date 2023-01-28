FROM debian

COPY entrypoint.sh /entrypoint.sh

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

RUN mkdir -p directory_api/api_requirements
COPY assets/requirements.txt directory_api/api_requirements/requirements.txt
RUN pip install -r directory_api/api_requirements/requirements.txt

## Copiar Implementación de la API
RUN mkdir -p directory_api/restdir && \
    mkdir -p auth_api/restauth && \
    mkdir -p common/restfs_common

ADD dir/dir_src directory_api/restdir
ADD auth/auth_src auth_api/restauth
ADD common/common_src common/restfs_common

# Copia de los setups de los paquetes
COPY common/setup.py common/setup.py
COPY auth/setup.py auth_api/setup.py
COPY dir/setup.py directory_api/setup.py

## Copiar Base de datos
COPY assets/db/data.db data.db 

## Copiar Script de lanzamiento
RUN mkdir -p directory_api/restdir_script
ADD scripts directory_api/restdir_script


## Lanzamiento entrypoint del docker

ENTRYPOINT [ "/bin/bash","entrypoint.sh" ]




