from django.conf.urls import url
from . import views

app_name = "villages"

urlpatterns = [
    url(r"^all/$", views.all, name="register"),
]