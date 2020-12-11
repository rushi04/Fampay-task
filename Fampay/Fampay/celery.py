from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fampay.settings')

app = Celery('Fampay', broker='redis://127.0.0.1:6379', include=['Fetch_Video.task'])
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'fetch_api',
        'schedule': 60.0,
    },
}
