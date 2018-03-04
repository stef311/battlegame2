from django.conf.urls import url
from . import views

app_name = "battle"

urlpatterns = [
    url(r"^dashboard/$", views.dashboard, name="dashboard"),
    url(r"^info/$", views.info, name="info"),
]