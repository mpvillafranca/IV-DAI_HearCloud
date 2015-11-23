# HearCloud

> Proyecto para las asignaturas IV y DAI consistente en una plataforma cloud de audio en la que sus usuarios pueden subir su música, escucharla y compartirla.

[![Build Status](https://travis-ci.org/mpvillafranca/hear-cloud.svg?branch=master)](https://travis-ci.org/mpvillafranca/hear-cloud)

## Introducción
**HearCloud** se trata de un proyecto para las asignaturas *Infraestructura Virtual* (IV) y *Diseño de Aplicaciones para Internet* (DAI) cuyo desarrollo será llevado a cabo a lo largo del año. Para ello, se hará uso de un framework de alto nivel (Django), teniendo en cuenta que la creación de toda la infraestructura virtual cumpla los objetivos de la asignatura IV: lenguajes de configuración, prueba, despliegue, integración continua, herramientas de construcción, entornos virtuales y testeo.

La aplicación consistirá en una plataforma cloud de audio en la que sus usuarios podrán subir su música, escucharla y compartirla con otros usuarios.

## Instalación

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
Se creará la infraestructura necesaria para la aplicación en la nube. En concreto, se prevee contar con:

1. Servidores web.
2. Servidores de base de datos.
3. Travis para trabajar con integración continua.

## Inscripción en el certamen de proyectos de la UGR organizado por la OSL

Proyecto inscrito en el [certamen de Proyectos Libres de la UGR 2015-2016](http://osl.ugr.es/bases-de-los-premios-a-proyectos-libres-de-la-ugr/)

![Imagen Inscripción](http://oi61.tinypic.com/k03vyc.jpg)

# Segundo hito

## Tecnologías utilizadas
Se ha decidido hacer uso del framework **Django** para el desarrollo de la aplicación, soportado por una base de datos **SQLite**. En un futuro, y en base a la funcionalidad esperada de la aplicación, quizas se integre una base de datos **MongoDB**, dejando la SQL para tareas como la gestión de usuarios.

## Herramienta de construcción
Python permite el uso de archivos como herramienta de construcción, de forma similar a como lo hacen otros leguajes.

## Integración continua y TDD
Se ha decidido seguir una metodología de desarrollo basado en pruebas (TDD), basándonos en la repetición de un tiempo muy corto de ciclo de desarrollo. De esta forma, creamos pruebas automatizadas que definen mejoras deseadas o nuevas funciones. A continuación, se produce una cantidad mínima de código para pasar esa prueba, y finalmente se refactoriza el código escrito. De esta forma, evitamos el código innecesario, pues solamente escribimos el mínimo código posible para pasar la prueba. Esto hará también más facil la modificación de código cuando el proyecto está en producción.

Para automatizar este proceso, se ha creado un archivo **Makefile**, de forma que llamando a `make test`, se llame a todos los comandos necesarios.

Para la integración continua, se ha utilizado Travis, que permite testear el código del proyecto de una manera facil y sencilla. Para ello, se accede a la página de Travis y basta con registrarse, haciendo uso de Github, y sincronizar el repositorio. Una vez generado y agregado al repositorio el archivo `travis.yml`, Travis se iniciará automáticamente, indicando si se pasan los tests o no.

# Tercer hito
Para el despliegue de la aplicación en un PaaS, hemos utilizado Heroku, debido a su facil integración con GitHub y por ser mayormente gratuita. Para realizar el deployment, necesitamos crear un fichero [Procfile](/Procfile) a la altura donde se encuentre nuestro `manage.py`.

	web: gunicorn hearcloud.wsgi

Una vez realizado todo esto, podemos acceder [aquí](https://hearcloud.herokuapp.com/) para comprobar que se ha desplegado correctamente.

## Contacto
Para cualquier consulta: mpvillafranca@correo.ugr.es
