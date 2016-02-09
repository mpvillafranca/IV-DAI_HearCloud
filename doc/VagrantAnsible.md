Configurando el despliegue en máquina virtual usando vagrant con el provisionador ansible
===
## Despliegue en un IaaS, Azure
Lo primero de todo es almacenar nuestro certificado de administración en Azure. Para ello, tal y como vemos [aquí](https://github.com/Azure/vagrant-azure/issues/65), ejecutamos lo siguiente:

```
$ openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout vagrant.key -out vagrant.key
$ openssl x509 -inform pem -in vagrant.key -outform der -out vagrant.cer
$ cat vagrant.key > vagrant.pem
```

Así, subiríamos el fichero `.cer` a Azure y el fichero `.pem`, debería tener la forma:

```
-----BEGIN CERTIFICATE-----
{pub key}
-----END CERTIFICATE-----
-----BEGIN RSA PRIVATE KEY-----
{private key}
-----END RSA PRIVATE KEY-----
```

El script `deploy.sh` descarga e instala lo necesario y empieza con el despligue haciendo uso de `Vagrant` y `Ansible`. Una vez creada y aprovisionada, lanza la ejecución de la aplicación mediante [Fabric](http://www.fabfile.org/). No obstante, primero deberemos introducir algunos de nuestros datos en dichos ficheros, como se detalla a continuación.

### Vagrant
Para la creación del [fichero Vagrantfile](../vagrant-azure/Vagrantfile) que levanta nuestra máquina en Azure, consultamos la documentación del plugin [aquí](https://github.com/Azure/vagrant-azure) y configuramos las variables que nos interesan. El usuario, deberá reemplazar tres de los valores que aquí aparecen por los suyos propios:

- `azure.mgmt_certificate`: aquí pondremos la ruta a nuestro `.pem`.
- `azure.subscription_id`: aquí pondremos la id de nuestra suscripción de Azure
- `azure.vm_password`: aquí pondremos la clave para el administrador la máquina. Esta misma contraseña, habrá que indicarla en el script [`deploy.sh`](../vagrant-azure/doploy.sh) para que Fabric tenga acceso a la máquina.

### Ansible
El aprovisionamiento de nuestra máquina se describe en el fichero `hearcloud.yml`, que puede consultarse [aquí](../vagrant-azure/hearcloud.yml). Además, en el archivo `ansible_hosts`, indicamos que trabajamos con una máquina localhost (pues estamos proveyendo la propia máquina). En concreto, las tareas que realiza son:

- Actualizar paquetes de repositorios. [Ref](http://docs.ansible.com/ansible/apt_module.html).
- Instalar en loop todos los paquetes necesarios, entre ellos, el sistema gestor de base de datos `postgresql` para que nuestra aplicación trabaje con él. [Ref](http://docs.ansible.com/ansible/playbooks_loops.html). Además:
    - Instalar el servidor web `gunicorn`, el cual es un servidor web wsgi que utilizaremos puesto que Django ya trae consigo un archivo `.wsgi`.
    - Instalar `nginx` para servir los archivos, balance de carga, restricciones de acceso, etc. La configuración de nginx se adjunta en el repositorio y consiste principalmente en un servidor web servidor web para archivos en  `/static` y un proxy inverso que se pasa a la aplicación wsgi.
    - Instalar `supervisord` para arrancar y mantener arrancado el servidor gnunicorn. De esta forma, supervisord vigilará que el proceso siempre esté ejecutandose.

### Fabric
Por último, el fichero fabfile.py de Fabric se encargará de:

- Copiar los archivos estáticos a su directorio correspondiente: `/var/etc/www`
- Copiar la configuración de nginx que se [adjunta en el repositorio](../vagrant-azure/production-webconfig/default) y consiste principalmente en un servidor web servidor web para archivos en `/static` y un proxy inverso que se pasa a la aplicación wsgi.
- Copiar la configuración de supervisord [adjunta también en el repositorio](../vagrant-azure/production-webconfig/supervisor.conf).
- Reiniciar ambos servicios.

Esta configuración para Django en producción es la que se propone [aquí](https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/gunicorn/) y [aquí](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-django-with-postgres-nginx-and-gunicorn).
