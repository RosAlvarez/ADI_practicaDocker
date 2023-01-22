# Trabajo teórico práctico 2: virtualización de servicios

## Virtualización de API: Directorio - Version DOCKER

Para la creación de la imágen del docker debemos ejecutar el siguiente script:

``` ./build.sh ```

Este además producirá un archivo **.tar.gz** con la imagen (debian-dirapi) comprimida. Tamaño: 237 MB

Una vez creada la imagen la lanzaremos con el siguiente script:

``` ./run.sh -u <uri_auth_server> -d <db_path> -a <token_admin> -l <address> -p <port> ```

Donde:

- <uri_auth_server>: argumento obligatorio, indica la URI donde se aloja el servicio de Autenticación.

- <db_path>: directorio donde se guardará la base de datos donde se almacena la información del servicio Directorio. Por defecto tomará el valor '/db' debiado a que se aloja en un volumen a parte.

- <token_admin>: token que corresponde a las operaciones de usuario del tipo administrador (Por defecto="admin").

- <address>: dirección IP donde se alojará el servicio Directorio (Por defecto="0.0.0.0").

- <port>: puerto donde escuchará el servicio Directorio (Por defecto=3002).

> Nota: debido a que estamos haciendo un mock del servicio de Autenticación, para que el servicio Directorio se lance correctamente debemos usar como token de administrador el token: **admin**. De lo contrario el servidor se cerrará ya que esa funcionalidad aun no está implementada.

## Ejmplo de utilzación

Una vez que el contenedor del servicio este funcionando, tras seguir los pasos anteriormente explicados, podremos probar la API RESTful de la siguiente manera:

1. Debemos hacer la instalación del proyecto python del cliente:

``` 
    cd ./client 
    python3 setup.py install
```
2. Una vez hecho esto, podremos utilizar el script de la primera entrega para probar la API:

```
    python3 ./scripts/client_script.py
```

> Nota: este script es un ejemplo que realiza un par de consultas/requests para comprobar que la API REST esta operativa, dicho script cuenta con algunas constantes que pueden ser modificadas como la dirección IP del contenedor para su correcto funcionamiento.

