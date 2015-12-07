from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False 
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
if HEROKU_ENVIRONMENT:
    import urlparse
    url = urlparse(os.environ["DATABASE_URL"])
    DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.postgresql_psycopg2',
	        'NAME': url.path[1:],
		    'USER': url.username,
		    'PASSWORD': url.password,
		    'HOST': url.hostname,
		    'PORT': url.port,
	    }
    }
elif TRAVIS_ENVIRONMENT:
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.postgresql_psycopg2',
            'NAME':     'travisdb',
            'USER':     'postgres',
            'PASSWORD': '',
            'HOST':     'localhost',
            'PORT':     '',
        }
    }
elif SNAP_CI_ENVIRONMENT:
    import urlparse
    url = urlparse(os.environ["SNAP_DB_PG_URL"])
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.postgresql_psycopg2',
	        'NAME': url.path[1:],
		    'USER': url.username,
		    'PASSWORD': url.password,
		    'HOST': url.hostname,
		    'PORT': url.port,
        }
    }

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = [BASE_DIR.child('static')]

SOCIAL_AUTH_FACEBOOK_KEY='519053204921748'
SOCIAL_AUTH_FACEBOOK_SECRET='f4716f67a0465d0f61ee3eca5a302e48'

#SOCIAL_AUTH_TWITTER_KEY=
#SOCIAL_AUTH_TWITTER_SECRET=
