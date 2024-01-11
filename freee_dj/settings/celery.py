import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freee_dj.settings.prod')
app = Celery('freee_dj')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()