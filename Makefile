install:
	sudo apt-get install python-dev
	pip install --upgrade pip 
	pip install -r requirements/local.txt

test: 
	python hearcloud/manage.py test apps.tests --settings=hearcloud.settings.local
	
run:
	python hearcloud/manage.py runserver --settings=hearcloud.settings.local
