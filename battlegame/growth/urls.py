from django.conf.urls import url
from . import views

app_name = "battle"

urlpatterns = [
    url(r"^(?P<village_id>[0-9]+)/academy/$", views.academy, name="academy"),
    url(r"^(?P<village_id>[0-9]+)/museum/$", views.museum, name="museum"),
]