from django.db import models

# Create your models here.
class NotificationModels(models.Model):
    message = models.TextField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message[:50]
    class Meta:
        verbose_name="Notification"