import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsboard.settings')
app = Celery('newsboard')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'cron-reset-upvote-amount': {
        'task': 'news.tasks.reset_upvote_amount',
        'schedule': crontab(minute=0, hour=0)
    },
}
app.conf.timezone = 'UTC'
