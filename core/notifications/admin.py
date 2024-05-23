from django.contrib import admin
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.urls.resolvers import URLPattern
from .models import NotificationModels
from django import forms
from django.shortcuts import HttpResponseRedirect
from django.urls import path
from notifications.tasks import run_task
# Register your models here.
class SendNotificationForm(forms.ModelForm):
    message = forms.CharField(
        label="Notification message",
        max_length=20,
    )
    class Meta:
        model = NotificationModels
        fields = ["message",]
@admin.register(NotificationModels)
class NotificationAdmin(admin.ModelAdmin):
    form = SendNotificationForm
    add_form_template = "admin/custom_add_notification_form.html"

    def add_view(self, request, form_url="send-notifications", extra_context=None):
        context = self.get_changeform_initial_data(request)
        if request.method == "POST":
            form = SendNotificationForm(request.POST)
            if form.is_valid():
                message = form.cleaned_data["message"]
                notification = NotificationModels.objects.create(message=message)
                run_task.delay(message)             
                
                return HttpResponseRedirect(f"../{notification.pk}")
            else:
                pass
        else:
            form = SendNotificationForm()
        context["form"] = form
        return super().add_view(request, form_url, extra_context=context)

    def get_urls(self):
        urls = super().get_urls()
        custom_url = [
            path("send-notification/", self.admin_site.admin_view(self.add_view), name='send-notification')
        ]
        print("--------------------")
        print(urls)
        return custom_url + urls
