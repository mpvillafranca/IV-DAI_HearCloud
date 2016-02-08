Configurando el despliegue en máquina virtual usando vagrant con el provisionador ansible
===

## Despliegue en un IaaS, Azure
En primer lugar, hemos de tener instalado el complemento que permite a vagrant administrar máquinas en azure. Si no lo tenemos instalado, ejecutamos:

```
$ vagrant plugin install vagrant-azure
```

A continuación, habría que logueatse en azure, accediendo al link e ingresando el código, y descargar nuestras credenciales, accediendo al enlace que nos proporciona la segunda orden:

```
$ azure login
$ azure account download
```

A continuación, importamos dichas credenciales a nuestro cliente de azure:

```
$ azure account import <nombre_fichero>
```

Además, generamos certificados SSL que se subirán a azure para poder interaccionar con él. Esto lo hacemos ejecutando:

```
$ openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout vagrant-azure.key -out vagrant-azure.key
$ chmod 600 ~/.ssh/vagrant-azure.key
$ openssl x509 -inform pem -in vagrant-azure.key -outform der -out vagrant-azure.cer
```

Una vez generado, subimos el fichero `vagrant-azure.cer` al apartado de _Certificados de administración_ de la web de azure.

Además, para que podamos autenticarnos en azure con el _Vagrantfile_, deberemos crear un nuevo archivo `.pem` con el contenido del archivo `.key`, para ello:

```
$ cat vagrant-azure.key > vagrant-azure.pem
```

Por último, nos proveemos de la box de Azure ejecutando:

```
$ vagrant box add azure https://github.com/msopentech/vagrant-azure/raw/master/dummy.box
```

### Vagrant
Ya estamos listos, ahora crearemos el archivo _Vagrantfile_, cuyo contenido puede consultarse [aquí](../vagrant-azure/Vagrantfile).

Con esto, realizamos tres tareas principalmente:

1. Indicamos que la _box_ que se va a usar es `azure`, que va a tener una red pública

2. Definimos las diferentes características de la máquina en azure, tales como el certificado, la imagen, el nombre de usuario, la localización o el mapeo de puertos.
3. Indicamos el provisionamiento de la máquina mediante ansible, el cual hace uso del archivo ansible-azure.yml.

No obstante, antes de ejecutar el comando `vagrant provider`, debemos definir la variable de entorno `ANSIBLE_HOSTS` (`export ANSIBLE_HOSTS = ...`).

### Ansible
El archivo `ansible-azure.yml`, que provee a la máquina azure de todo lo necesario para la ejecución de nuestra aplicación, puede consultarse [aquí](../vagrant-azure/ansible-azure.yml).

Además, en el archivo `ansible_hosts`, indicamos que trabajamos con una máquina localhost (pues estamos proveyendo la propia máquina).

El provisionamiento en concreto consiste en:

- Instalar el sistema gestor de base de datos `postgresql` para que nuestra aplicación trabaje con él.
- Instalar el servidor web `gunicorn`, el cual es un servidor web wsgi que utilizaremos puesto que Django ya trae consigo un archivo `.wsgi`.
- Instalar `nginx` para servir los archivos, balance de carga, restricciones de acceso, etc. La configuración de nginx se adjunta en el repositorio y consiste principalmente en un servidor web servidor web para archivos en  `/static` y un proxy inverso que se pasa a la aplicación wsgi.
- Instalar `supervisord` para arrancar y mantener arrancado el servidor gnunicorn. De esta forma, supervisord vigilará que el proceso siempre esté ejecutandose.

Finalmente, solo faltaría ejecutar `vagrant up --provider=azure`.
