from pathlib import Path
import os, sys


BASE_DIR = Path(__file__).resolve().parent.parent

PROJECT_ROOT = os.path.dirname(__file__)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ysl(888^duj6c@()&p=vc)es!559e&y_mvjg&4&i&lg^#&s_9s'

DEBUG = False

ALLOWED_HOSTS = ['77.222.42.39']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'products_dj',
        'USER': 'aadmin',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../static')