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

RUN mkdir -p api_requirements
COPY assets/requirements.txt api_requirements/requirements.txt
RUN pip install -r api_requirements/requirements.txt


## Copiar Implementación de la API
RUN mkdir -p restdir
ADD src restdir

## Copiar Base de datos
COPY assets/db/data.db /data.db 

## Copiar Script de lanzamiento
RUN mkdir -p restdir_script
ADD script restdir_script

COPY setup.py setup.py

## Lanzamiento entrypoint del docker

ENTRYPOINT [ "/bin/bash","entrypoint.sh" ]




