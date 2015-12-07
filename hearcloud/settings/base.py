# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from unipath import Path
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
    

BASE_DIR = Path(__file__).ancestor(3)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0q0ax-!_=#tucxt%%-nerf1r4k4do18e%d72=&+l-08-w+_pzk'

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
