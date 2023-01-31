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
RUN mkdir -p directory_api/restdir
ADD src directory_api/restdir

## Copiar Base de datos
COPY assets/db/data.db data.db 

## Copiar Script de lanzamiento
RUN mkdir -p directory_api/restdir_script
ADD scripts directory_api/restdir_script

COPY setup.py directory_api/setup.py

## Lanzamiento entrypoint del docker

ENTRYPOINT [ "/bin/bash","entrypoint.sh" ]




