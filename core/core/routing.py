from django.urls import path
from notifications.consumers import NotificationsConsumer
websocket_urlpatterns = [
    path(
        "ws/notifications/", NotificationsConsumer.as_asgi()
    )  # This endpoint will be used to create a websocket that we would point our websocket to
]
