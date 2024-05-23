from celery import group
from notifications.tasks import *
tasks_group = group(tp1.s(), tp2.s(), tp3.s(), tp4.s())
tasks_group.apply_async()

from celery import chain