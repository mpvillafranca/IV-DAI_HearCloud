"""
WSGI config for hearcloud project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

ON_HEROKU = os.environ.get('PORT')
if ON_HEROKU:
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hearcloud.settings.staging")
	application = Cling(get_wsgi_application())
else:
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hearcloud.settings.local")
	application = get_wsgi_application()

