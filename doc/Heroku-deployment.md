## Despliegue en un PaaS: [Heroku](https://www.heroku.com)
Para realizar el respliegue, debemos realizar algunas configuraciones.

En primer lugar, un fichero [Procfile](../Procfile) y un fichero con las dependencias `requirements.txt`.

Por último, ejecutamos un script que automatice el proceso de despliegue:

```
wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
heroku login
heroku create
git add .
git commit -m "despliegue en heroku"
git push heroku master
heroku ps:scale web=1
heroku open
```

Además, incluimos la integración contínua, de modo que cada vez que hagamos un cambio en el repositorio, se realice el despliegue de forma automática. Para ello, utilizamos SNAP CI.

Desde la interfaz web, realizamos la siguiente configuración:

![SNAP_CI]()

Y, con esto, conseguimos tener integración contínua que despliega la aplicación al hacer `git push` en Github, siempre que esta pase los tests.
