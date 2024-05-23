from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import time
@shared_task
def run_task(message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notifications", {"type": "send_notification", "message": message}
    )
    return message
@shared_task
def tp1(queue="celery"):
    time.sleep(3)
    return


@shared_task
def tp2(queue="celery:1"):
    time.sleep(3)
    return


@shared_task
def tp3(queue="celery:2"):
    time.sleep(3)
    return


@shared_task
def tp4(queue="celery:3"):
    time.sleep(3)
    return


