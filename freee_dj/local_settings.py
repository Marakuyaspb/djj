from pathlib import Path
import os, sys


BASE_DIR = Path(__file__).resolve().parent.parent

PROJECT_ROOT = os.path.dirname(__file__)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ysl(oab^duj6c@()&p=vc)es!559e&y_mvjg&4&i&lg^#&s_9s'

DEBUG = True

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'products': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db5_test.db',
        # 'USER': 'admin',
        # 'PASSWORD': '123',
    }
}

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../static')