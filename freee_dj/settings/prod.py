import os
from .base import *


DEBUG = True

ALLOWED_HOSTS = [
    '77.222.42.39',
    '77-222-42-39.swtest.ru'
]

    
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'products_dj',
        'USER': 'user',
        'PASSWORD': 'pass',
        'HOST': '77.222.42.39',
        'PORT': '5432',
    }
}

ADMINS = [
    ('Annaa', 'fflaminfo@gmail.com'),
]


REDIS_URL = 'redis://cache:6379'
CACHES['default']['LOCATION'] = REDIS_URL
CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]