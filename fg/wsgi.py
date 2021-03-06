import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fg.settings")

application = get_wsgi_application()

import django_rq
from datetime import datetime
from fg.apps.main.utils import backup_db
scheduler = django_rq.get_scheduler('default')
scheduled_jobs = list(scheduler.get_jobs())

# Do we have the backup database job?
found_jobs = [x for x in scheduled_jobs if x.meta.get('name') == 'backup_db']
if len(found_jobs) == 0:
    print("Scheduling daily backups with django-rq...")
    job = scheduler.schedule(
        scheduled_time=datetime.utcnow(), # Time for first execution
        func=backup_db,                   # Function to be queued
        interval=86400,                   # Seconds before the function is called again (one day)
        repeat=None,                      # Repeat this number of times (None means repeat forever)
        meta={'name': 'backup_db'}        # Arbitrary pickleable data on the job itself
    )
