from fabric.api import run

def runserver():
    run('cd hear-cloud && python manage.py migrate --settings=hearcloud.productionsettings')
    run('sudo mkdir -p /var/www')
    run('cd hear-cloud && sudo cp -r static/ /var/www/static')
    run('cd hear-cloud && sudo cp vagrant-azure/production-webconfig/default /etc/nginx/sites-available/')
    run('cd hear-cloud && sudo cp vagrant-azure/production-webconfig/supervisor.conf /etc/supervisor/conf.d/')
    run('sudo service nginx restart')
    run('sudo service supervisor restart')
