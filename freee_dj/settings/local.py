from .base import *

# for local dev:
# python3 manage.py runserver --settings=freee_dj.settings.local

DEBUG = True
ALLOWED_HOSTS = [
    '127.0.0.1',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}