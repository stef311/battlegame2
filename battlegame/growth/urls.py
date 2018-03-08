from django.urls import path
from . import views

app_name = "growth"

urlpatterns = [
    path("<int:village_id>/academy/", views.academy, name="academy"),
    path("<int:village_id>/museum/", views.museum, name="museum"),
]