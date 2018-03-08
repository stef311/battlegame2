from django.conf.urls import url
from . import views

app_name = "servers"

urlpatterns = [
    url(r"^$", views.server_list, name="server_list"),
    url(r"^create/$", views.server_create, name="server_create"),

]