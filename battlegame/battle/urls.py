from django.urls import path
from . import views

app_name = "battle"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("overview/", views.overview, name="overview"),
]