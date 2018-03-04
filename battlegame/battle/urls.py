from django.conf.urls import url
from . import views

app_name = "battle"

urlpatterns = [
    url(r"^dashboard/$", views.dashboard, name="dashboard"),
    url(r"^info/$", views.info, name="info"),
    url(r"^central/$", views.info, name="central"),
    url(r"^army/$", views.info, name="army"),
    url(r"^market/$", views.info, name="market"),

]