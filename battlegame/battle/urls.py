from django.conf.urls import url
from . import views

app_name = "battle"

urlpatterns = [
    url(r"^dashboard/$", views.dashboard, name="dashboard"),
    url(r"^info/$", views.info, name="info"),
    url(r"^central/$", views.central_building, name="central"),
    url(r"^army/$", views.army_building, name="army"),
    url(r"^market/$", views.market_building, name="market"),

]