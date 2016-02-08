# HearCloud

> Plataforma cloud de audio en la que sus usuarios pueden subir su música, escucharla y compartirla.

[![Build Status](https://travis-ci.org/mpvillafranca/hear-cloud.svg?branch=master)](https://travis-ci.org/mpvillafranca/hear-cloud)
[![Snap CI](https://snap-ci.com/mpvillafranca/hear-cloud/branch/master/build_image)](https://snap-ci.com/mpvillafranca/hear-cloud/branch/master)
[![Heroku](https://www.herokucdn.com/deploy/button.png)](http://hearcloud.herokuapp.com/)
[![Azure](https://camo.githubusercontent.com/9285dd3998997a0835869065bb15e5d500475034/687474703a2f2f617a7572656465706c6f792e6e65742f6465706c6f79627574746f6e2e706e67)](http://hearcloud.cloudapp.net)

## Introducción
**HearCloud** es un proyecto de plataforma cloud de audio, donde sus usuarios pueden subir su música, escucharla, organizarla y bajársela de nuevo en todo momento, desarrollada con un framework de alto nivel (Django) teniendo en cuenta que la creación de toda la Infraestructura Virtual (IV) cumple los objetivos marcados: lenguajes de configuración, prueba, despliegue, integración continua, herramientas de construcción, entornos virtuales y testeo.

## Instalación

Para instalar la apliación en un entorno local, realizar los siguientes pasos:

Clonar en tu equipo:

    git clone git@github.com:mpvillafranca/hear-cloud.git

Instalar las dependencias:

    sudo apt-get install python-dev
    pip install --upgrade pip
    pip install -r requirements.txt

Realizar las migraciones de la base de datos y lanzar el servidor:

    python manage.py migrate
    python manage.py runserver

## Infraestructura
En cuanto a la infraestructura de la apliación, se prevee realizar el despliegue sobre una plataforma en la nube del tipo Azure o Amazon AWS, donde contaremos con servidores web y servidores de base de datos.

Además, los servidores web y de base de datos podrán no encontrarse necesariamente en la misma máquina, con el fin de repartir carga y proveer de mayor seguridad.

Como base de datos back-end, utilizamos PostgreSQL y como lenguaje de programación, utilizamos Python y Django como framework para agilizar el desarrollo web. 

Además, debemos ser capaces de realizar un despliegue correcto de la plataforma sobre cualquier infraestructura virtual.

## Integración contínua
Puesto que estamos realizando un desarrollo basado en pruebas (TDD), debemos elegir un sistema de integración contínua, de modo que cada cambio realizado en el repositorio implique una ejecución de los tests, asegurándonos que todo el código escrito funciona correctamente.

En este caso, utilizamos [Travis](https://travis-ci.org/), que es una alternativa sencilla pero muy completa para ello. Aunque existen otras como [Jenkins](https://jenkins-ci.org/) o [Shippable](https://www.shippable.com/).

Para más información, hacer [click aquí](./doc/Integracion-continua.md).

## Despliegue en un PaaS: [Heroku](https://www.heroku.com)
Como parte del desarrollo de la apliación, decimimos realizar un deployment a Heroku, ya que es bastante sencillo de realizar y nos permite comprobar que nuestra apliación funciona desde primera hora correctamente.

Podemos consultar el resultado en: [https://hearcloud.herokuapp.com/](https://hearcloud.herokuapp.com/).

Para más información, hacer [click aquí](./doc/Heroku-deployment.md).

## Entorno de pruebas: [Docker](https://www.docker.com/)

Docker es una herramienta que permite automatizar el despliegue de aplicaciones dentro de contenedores software, lo cual facilita probarla en un entorno aislado para su posterior despliegue a producción. 

Podemos acceder a la imagen de la aplicación creada haciendo [click aquí](https://hub.docker.com/r/mpvillafranca/hearcloud/). A continuación, para crear el entorno de pruebas, basta con ejecutar los siguientes comandos:

```
sudo apt-get update
sudo apt-get install -y docker.io
sudo docker pull mpvillafranca/hearcloud
sudo docker run -t -i mpvillafranca/hearcloud /bin/bash
```

Para más información, hacer [click aquí](./doc/Docker.md).

## Despliegue automático en un IaaS: Azure
Para realizar un despliegue automático en un IaaS como Azure, hacemos uso de dos herramientas básicas: `Vagrant` para la creación y configuración de la máquina virtual y `Ansible` para su aprovisionamiento. Para ello, creamos los correspondientes ficheros `Vagrantfile` y `.yml` de ansible.

Todo esto se ha unificado en un solo script, y basta con ejecutarlo para crear de forma automática la máquina en azure, aprovisionarla y lanzar el servidor que corra nuestra aplicación:

```
$ ./deploy-azure.sh
```

Para más información, hacer [click aquí](./doc/VagrantAnsible.md).


## Inscripción en el certamen de proyectos de la UGR organizado por la OSL

Este proyecto se encuentra inscrito en el [certamen de Proyectos Libres de la UGR 2015-2016](http://osl.ugr.es/bases-de-los-premios-a-proyectos-libres-de-la-ugr/)

![Imagen Inscripción](http://oi61.tinypic.com/k03vyc.jpg)

## Contacto
Para cualquier consulta: mpvillafranca@correo.ugr.es
