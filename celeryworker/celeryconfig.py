import os

CELERY_BROKER_URL = "amqp://guest:guest@rabbitmq:5672/"
result_backend = "redis://redis:6379/0"
