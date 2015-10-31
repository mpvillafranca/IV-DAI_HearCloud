test: 
	python hearcloud/manage.py test apps.tests --settings=hearcloud.settings.local
	
run:
	python hearcloud/manage.py runserver --settings=hearcloud.settings.local
