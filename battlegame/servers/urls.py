from django.urls import path
from . import views

app_name = "servers"

urlpatterns = [
    path("list/", views.server_list, name="server_list"),
    path("create/", views.server_create, name="server_create"),
    path("<int:server_id>/join/", views.server_join, name="server_join"),
]
