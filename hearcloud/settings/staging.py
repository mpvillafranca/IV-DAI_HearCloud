from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False 
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
	'default': {
	    'ENGINE': 'django.db.backends.postgresql_psycopg2',
	    'NAME': 'dfk2oo5e440rm1',
		'USER': 'upqwtyepgkxgyl',
		'PASSWORD': 'rMBhKn9XlYICwlsNboUgZIFAWZ',
		'HOST': 'ec2-50-16-229-89.compute-1.amazonaws.com',
		'PORT': '5432',
	}
}

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = [BASE_DIR.child('static')]

SOCIAL_AUTH_FACEBOOK_KEY='519053204921748'
SOCIAL_AUTH_FACEBOOK_SECRET='f4716f67a0465d0f61ee3eca5a302e48'

#SOCIAL_AUTH_TWITTER_KEY=
#SOCIAL_AUTH_TWITTER_SECRET=
