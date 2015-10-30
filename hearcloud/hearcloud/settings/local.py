from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True 

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child('hearcloud_db.sqlite3'),
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

SOCIAL_AUTH_FACEBOOK_KEY='519053204921748'
SOCIAL_AUTH_FACEBOOK_SECRET='f4716f67a0465d0f61ee3eca5a302e48'

#SOCIAL_AUTH_TWITTER_KEY=
#SOCIAL_AUTH_TWITTER_SECRET=
