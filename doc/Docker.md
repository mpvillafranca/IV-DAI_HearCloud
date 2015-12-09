Entorno de pruebas: [Docker](https://www.docker.com/)
===

A la hora de crear la imagen de la aplicación, Docker hace uso del fichero Dockerfile situado en el raiz del repositorio. Su contenido es el siguiente:

```
FROM ubuntu:latest

#Autor
MAINTAINER Mariano Palomo Villafranca <mpvillafranca@correo.ugr.es>

#Actualizar el sistema
RUN sudo apt-get -y update

#Instalar git y descargar la aplicacion
RUN sudo apt-get install -y git
RUN sudo git clone https://github.com/mpvillafranca/hear-cloud.git

# Instalar Python y PostgreSQL
RUN sudo apt-get install -y python-setuptools
RUN sudo apt-get -y install python-dev
RUN sudo apt-get -y install build-essential
RUN sudo apt-get -y install python-psycopg2
RUN sudo apt-get -y install libpq-dev
RUN sudo easy_install pip
RUN sudo pip install --upgrade pip

#Instalamos las dependencias y la aplicacion
RUN cd hear-cloud/ && sudo pip install -r requirements.txt

#Realizamos migraciones
RUN cd hear-cloud/ && python manage.py syncdb --noinput
```

A continuación, en la web de Docker Hub, creamos un _Automated Build_ con el repositorio de nuestro proyecto, lo cual nos genera [esta imagen](https://hub.docker.com/r/mpvillafranca/hearcloud/). De este modo, cualquier cambio realizado sobre el código del repositorio, se integrará de forma automática mediante Docker Hub, que rehará el build de la imagen por cada "git push" que hagamos.

Para crear el entorno de pruebas en nuestro ordenador, se debeǹ ejecutar los comando:

```
sudo apt-get update
sudo apt-get install -y docker.io
sudo docker pull mpvillafranca/hearcloud
sudo docker run -t -i mpvillafranca/hearcloud /bin/bash
```
