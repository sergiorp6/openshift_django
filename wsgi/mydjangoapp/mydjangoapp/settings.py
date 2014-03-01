"""
Django settings for mydjangoapp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from socket import gethostname

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ON_OPENSHIFT = False
if os.environ.get('OPENSHIFT_REPO_DIR'):
    ON_OPENSHIFT = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's@!t^l%%x=7$hi6c!k@eblze$dg9)esv@!8@vworriw@!#o5a&'

# SECURITY WARNING: don't run with debug turned on in production!
if ON_OPENSHIFT:
    DEBUG = False
    TEMPLATE_DEBUG = False
else:
    DEBUG = True
    TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["*"]

'''
Note that the above is a bit of a security risk.  You'll want to change this to something like:

ALLOWED_HOSTS = [
  gethostname(), # For internal OpenShift load balancer security purposes.
  os.environ.get('OPENSHIFT_APP_DNS',''), # Dynamically map to the OpenShift gear name.
  'ex-std-node.prod.rhcloud.com',
  'yoursite.com',
]
'''
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    're',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mydjangoapp.urls'

WSGI_APPLICATION = 'mydjangoapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# TODO: replace the credentials below with your dev and prod 
#	info

if ON_OPENSHIFT:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'x',
	'NAME': 'x',
	'PASSWORD':'x',
	'HOST': os.environ.get('OPENSHIFT_MYSQL_DB_HOST',''),
	'PORT': os.environ.get('OPENSHIFT_MYSQL_DB_PORT',''),

        'OPTIONS': {
             'init_command': 'SET storage_engine=INNODB',
        }
     }
    }
else:
    DATABASES = {
     'default': {
	'ENGINE': 'django.db.backends.mysql',
	'USER': 'root',
	'NAME': 'web',
	'PASSWORD':'x',
	'HOST': 'localhost',
	'PORT': ''
     }
  }


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_FAIL_SILENTLY = not DEBUG

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "../static")
TEMPLATE_DIRS = (
	os.path.join(BASE_DIR, "templates"),

)

#TODO: replace the credentials with your own SMTP server
#	or sign up for a free one at mailgun.org
#	Note that these settings will work with mailgun on 
#	openshift once you setup your mailgun account.
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your_user'
EMAIL_HOST_PASSWORD = 'your_password'
#EMAIL_USE_TLS = False
