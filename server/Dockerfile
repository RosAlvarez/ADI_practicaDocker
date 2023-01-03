FROM debian

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

## Implementación de la API
RUN mkdir -p restdir
ADD src restdir

## Base de datos
RUN mkdir -p db
COPY assets/db/data.db db/data.db

## Script de lanzamiento
RUN mkdir -p restdir_script
COPY script/server_script.py restdir_script/server_script.py

COPY setup.py setup.py

ENTRYPOINT [ "entrypoint.sh" , "admin"]




