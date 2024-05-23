import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core", broker="amqp://guest@localhost//")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.task_routes = {
    "notifications.tasks.*": {"queue": "queue1"},
    "notifications.tasks.task2": {"queue": "queue2"},
}

app.conf.broker_transport_options = {
    "priority_steps": list(range(0, 10)),
    "sep": ":",
    "queue_order_strategy": "priority",
}
app.autodiscover_tasks()
