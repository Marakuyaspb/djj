import os
from .base import *


DEBUG = False

ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'products_dj',
        'USER': 'contentman',
        'PASSWORD': 'Sofa1924Power!',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

ADMINS = [
    ('Annaa', 'fflaminfo@gmail.com'),
]


REDIS_URL = 'redis://cache:6379'
CACHES['default']['LOCATION'] = REDIS_URL
CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]