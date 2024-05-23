from django.shortcuts import render

# Create your views here.
def notification_page(request):
    return render(request, "core/notification_page.html")