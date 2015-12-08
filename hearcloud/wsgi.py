"""
WSGI config for hearcloud project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

LOCAL_DEVELOPMENT = True
HEROKU_ENVIRONMENT, TRAVIS_ENVIRONMENT, SNAP_CI_ENVIRONMENT = False, False, False

if 'HEROKU_ENVIRONMENT' in os.environ:
    LOCAL_DEVELOPMENT = False
    HEROKU_ENVIRONMENT = True
elif 'TRAVIS' in os.environ:
    LOCAL_DEVELOPMENT = False
    TRAVIS_ENVIRONMENT = True
elif 'SNAP_CI' in os.environ:
    LOCAL_DEVELOPMENT = False
    SNAP_CI_ENVIRONMENT = True

if not HEROKU_ENVIRONMENT:
    env = os.environ

from django.core.wsgi import get_wsgi_application

if LOCAL_DEVELOPMENT:
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hearcloud.settings.local")
	application = get_wsgi_application()
else:
    from dj_static import Cling
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hearcloud.settings.staging")
	application = Cling(get_wsgi_application())
