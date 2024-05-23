from celery import Celery
app = Celery("task")
app.config_from_object("celeryconfig", namespace="CELERY")
app.conf.imports = ("notifications.tasks")
app.autodiscover_tasks()


@app.task(bind=True)
def add_numbers():
    return 2+2