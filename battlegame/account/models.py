from django.db import models
from django.conf import settings
from .appconfig import CLASS_CHOICES

# Create your models here.

class Profile(models.Model):

    tribe = models.IntegerField(choices=CLASS_CHOICES, default=1)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    description = models.TextField()

