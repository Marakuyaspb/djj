import os
from celery import Celery
# задать стандартный модуль настроек Django
# для программы 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freee_dj.settings')
app = Celery('freee_dj')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()