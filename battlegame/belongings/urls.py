from django.conf.urls import url
from . import views

app_name = "belongings"

urlpatterns = [
    url(r"^overview/$", views.overview, name="overview"),
    url(r"^market/$", views.market, name="market"),
    url(r"^resource_exchange/$", views.resource_exchange, name="resource_exchange"),
    url(r"^warehouse/$", views.warehouse, name="warehouse"),

]