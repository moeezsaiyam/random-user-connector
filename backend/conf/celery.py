from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

# Load the default settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

# initiate a celery app
app = Celery('user_connector')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
