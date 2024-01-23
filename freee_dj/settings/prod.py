import os
from .base import *


DEBUG = False

ALLOWED_HOSTS = [
    '77.222.42.39',
    '77-222-42-39.swtest.ru'
]

    
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'prod',
        'USER': 'postgres',
        'PASSWORD': 'JustVery19JanyarySecurePass!',
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