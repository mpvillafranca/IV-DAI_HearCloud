# HearCloud

> Plataforma cloud de audio en la que sus usuarios pueden subir su música, escucharla y compartirla.

[![Build Status](https://travis-ci.org/mpvillafranca/hear-cloud.svg?branch=master)](https://travis-ci.org/mpvillafranca/hear-cloud)
[![Snap CI](https://snap-ci.com/mpvillafranca/hear-cloud/branch/master/build_image)](https://snap-ci.com/mpvillafranca/hear-cloud/branch/master)
[![Heroku](https://www.herokucdn.com/deploy/button.png)](http://hearcloud.herokuapp.com/)

## Introducción
**HearCloud** es un proyecto de plataforma cloud de audio, donde sus usuarios pueden subir su música, escucharla y compartirla, desarrollada con un framework de alto nivel (Django) teniendo en cuenta que la creación de toda la Infraestructura Virtual (IV) cumple los objetivos marcados: lenguajes de configuración, prueba, despliegue, integración continua, herramientas de construcción, entornos virtuales y testeo.

## Instalación

Para instalar la apliación en un entorno local, realizar los siguientes pasos:

Clonar en tu equipo:

    git clone git@github.com:mpvillafranca/hear-cloud.git

Instalar las dependencias:

    sudo apt-get install python-dev
    pip install --upgrade pip
    pip install -r requirements/local.txt

Sincronizar la base de datos y lanzar el servidor:

    python manage.py syncdb --settings=hearcloud.settings.local
    python manage.py runserver --settings=hearcloud.settings.local

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

Para más información, hacer [click aquí](./doc/Heroku-.md).

## Inscripción en el certamen de proyectos de la UGR organizado por la OSL

Este proyecto se encuentra inscrito en el [certamen de Proyectos Libres de la UGR 2015-2016](http://osl.ugr.es/bases-de-los-premios-a-proyectos-libres-de-la-ugr/)

![Imagen Inscripción](http://oi61.tinypic.com/k03vyc.jpg)

## Contacto
Para cualquier consulta: mpvillafranca@correo.ugr.es
