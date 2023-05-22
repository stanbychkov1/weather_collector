import os

from celery import Celery
from celery.signals import worker_ready
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'weather_collector.settings')

app = Celery('dwe')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@worker_ready.connect
def at_start(sender, **k):
    with sender.app.connection() as conn:
        sender.app.send_task('weather_collector')
