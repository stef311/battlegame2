from django.conf.urls import url
from . import views

app_name = "belongings"

urlpatterns = [
    url(r"^overview/$", views.overview, name="overview"),
]