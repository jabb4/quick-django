import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app')
app.conf.enable_utc = False
app.conf.update(timezone=os.environ.get("TIMEZONE"))
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()