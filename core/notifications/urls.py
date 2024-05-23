from django.urls import path
from .views import notification_page

app_name = 'notification_app'
urlpatterns = [
    path("", notification_page, name="notification_page"),
]
