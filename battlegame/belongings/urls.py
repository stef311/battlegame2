from django.urls import path
from . import views

app_name = "belongings"

urlpatterns = [
    path("overview/", views.overview, name="overview"),
    path("market/", views.market, name="market"),
    path("resource_exchange/", views.resource_exchange, name="resource_exchange"),
    path("warehouse/", views.warehouse, name="warehouse"),

]