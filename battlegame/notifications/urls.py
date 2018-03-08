from django.urls import path
from . import views

app_name = "notifications"

urlpatterns = [
    path("message_list/", views.message_list, name="message_list"),
    path("notification_list/", views.notification_list, name="notification_list"),

]
