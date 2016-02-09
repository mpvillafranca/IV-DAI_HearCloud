# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.core.exceptions import ImproperlyConfigured
from unipath import Path
import os
import json
BASE_DIR = Path(__file__).ancestor(2)

with open("hearcloud/secrets.json") as f:
    secrets = json.loads(f.read())
    
def get_secret(secret_name, secrets = secrets):
    try:
        return secrets[secret_name]
    except:
        msg = "La variable %s no existe" % secret_name
        raise ImproperlyConfigured(msg)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('SECRET_KEY')

# Application definition
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
	'social.apps.django_app.default',
)

LOCAL_APPS = (
	'apps.home',
	'apps.users',
	'apps.tests',
	'apps.stream',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'hearcloud.urls'

WSGI_APPLICATION = 'hearcloud.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = [BASE_DIR.child('templates')]

AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = (
	'social.backends.facebook.FacebookAppOAuth2',
	'social.backends.facebook.FacebookOAuth2',
	#'social.backends.twitter.TwitterOAuth',
	'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/' # Despues de login
SOCIAL_AUTH_LOGIN_URL = '/error/' # Cuando se produzcan errores
SOCIAL_AUTH_USER_MODEL = 'users.User'
SOCIAL_AUTH_FACEBOOK_SCOPE=['email']
FACEBOOK_EXTENDED_PERMISSIONS = ['email']

STATIC_URL = '/static/'
STATIC_ROOT = '/etc/www/static'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEBUG = True
TEMPLATE_DEBUG = True 
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hearcloud',
        'USER': 'dbuser',
        'PASSWORD':'12345678',
        'HOST': 'localhost',
        'PORT': '',
    }
}

SOCIAL_AUTH_FACEBOOK_KEY = get_secret('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = get_secret('SOCIAL_AUTH_FACEBOOK_SECRET')
