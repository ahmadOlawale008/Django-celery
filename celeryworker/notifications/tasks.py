from celery import shared_task
@shared_task
def task1():
    return "Task 1"


@shared_task
def task2():
    return "Task 2"
