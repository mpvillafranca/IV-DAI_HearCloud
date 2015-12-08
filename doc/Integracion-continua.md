Integración continua
===
Utilizamos Travis para introducir integración continua en nuestro repositorio. Para ello, incluimos un fichero `.yml` en el raíz del repositorio con la configuración correspondiente.

## Travis
Creamos el fichero [`travis.yml`](../travis.yml) que quedaría como sigue:

```
# Lenguaje de programacion 
language: python

# Version Python
python:
  - "2.7" 

# Servicios a usar
services: postgresql

# Provisionamiento de la maquina
install:
  - sudo apt-get install python-dev
  - pip install --upgrade pip
  - pip install -r requirements.txt

# Acciones antes de comenzar las pruebas
before_script:
  - psql -c "CREATE DATABASE travisdb;" -U postgres

# Ejecucion de pruebas
script:
  - python manage.py test apps.tests

# Ejecutamos solo los test de la rama master del repositorio
branches:
  - only:
    - master

# Notificamos los resultados de los test por correo
notifications:
  email:
    on_success: change
    on_failure: always
```

