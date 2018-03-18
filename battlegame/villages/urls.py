from django.urls import path
from . import views

app_name = "villages"

urlpatterns = [
    path("all/", views.all, name="all"),
    path("main/<int:village_id>", views.main, name="main")
]