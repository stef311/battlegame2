from django.db import models
from django.conf import settings

# Create your models here.

class Village(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    attack_power = models.IntegerField(default=0)
    defense_power = models.IntegerField(default=0)
    population = models.IntegerField(default=0)
    culture = models.IntegerField(default=0)
    science = models.IntegerField(default=0)
    description = models.CharField(max_length=2000)


