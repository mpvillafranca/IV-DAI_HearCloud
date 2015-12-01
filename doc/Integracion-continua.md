Integración continua
===
Utilizamos dos alternativas diferentes para introducir integración continua en nuestro repositorio: Travis y Shippable. Para ambas, incluimos un fichero `.yml` en el raíz del repositorio con la configuración correspondiente.

## Travis
Creamos el fichero [`travis.yml`](../travis.yml) que quedaría como sigue:

```
# Lenguaje de programacion 
language: python

# Version Python
python:
  - "2.7" 

# Provisionamiento de la maquina
install:
  - sudo apt-get install python-dev
  - pip install --upgrade pip
  - pip install -r requirements/staging.txt

# Ejecucion de pruebas
script:
  - python manage.py test apps.tests --settings=hearcloud.settings.staging

# Ejecutamos solo los test de la rama master del repositorio
branches:
  - only:
    - master

# Notificamos los resultados de los test por correo
notifications:
  recipients:
    - mpvillafranca@correo.ugr.es
  email:
    on_success: change
    on_failure: always
```


## Shippable
Creamos el fichero [`shippable.yml`](../shippable.yml) con la siguiente configuración:

```
# Distribucion de desarrollo
build_environment: Ubuntu 14.04

# Lenguaje de programacion
language: python

# Version Python
python:
  - "2.7"

# Provisionamiento de la maquina
install:
  - sudo apt-get install python-dev
  - pip install --upgrade pip
  - pip install -r requirements/staging.txt

# Ejecucion de pruebas
script:
 - python manage.py test apps.tests --settings=hearcloud.settings.staging
```
