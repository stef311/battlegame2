from django.conf.urls import url
from . import views

app_name = "battle"

urlpatterns = [
    url(r"^academy/$", views.academy, name="academy"),
    url(r"^museum/$", views.museum, name="museum"),
]