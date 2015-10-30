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

    python hearcloud/manage.py syncdb --settings=hearcloud.settings.local
    python hearcloud/manage.py runserver --settings=hearcloud.settings.local

## Infraestructura
Se creará la infraestructura necesaria para la aplicación en la nube. En concreto, se prevee contar con:

1. Servidores web.
2. Servidores de base de datos.
3. Travis para trabajar con integración continua.

## Inscripción en el certamen de proyectos de la UGR organizado por la OSL

Proyecto inscrito en el [certamen de Proyectos Libres de la UGR 2015-2016](http://osl.ugr.es/bases-de-los-premios-a-proyectos-libres-de-la-ugr/)

![Imagen Inscripción](http://oi61.tinypic.com/k03vyc.jpg)

## Contacto
Para cualquier consulta: mpvillafranca@correo.ugr.es
