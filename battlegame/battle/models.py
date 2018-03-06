from django.db import models
from django.conf import settings

class UnitType(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    name = models.CharField(max_length=20)
    attack_power = models.IntegerField(default=0)
    defense_power = models.IntegerField(default=0)
    population = models.IntegerField(default=0)
    culture = models.IntegerField(default=0)
    science = models.IntegerField(default=0)
    wood = models.IntegerField(default=0)
    iron = models.IntegerField(default=0)
    wood_per_turn = models.IntegerField(default=0)
    iron_per_turn = models.IntegerField(default=0)
    silver = models.IntegerField(default=0)
    description = models.CharField(max_length=2000)