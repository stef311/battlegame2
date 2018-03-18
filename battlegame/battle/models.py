from django.db import models
from django.conf import settings

class Unit(models.Model):
    name = models.CharField(max_length=20)
    attack_power = models.IntegerField(default=0)
    defence_power = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    population = models.IntegerField(default=0)
    culture = models.IntegerField(default=0)
    science = models.IntegerField(default=0)
    wood = models.IntegerField(default=0)
    iron = models.IntegerField(default=0)
    wood_per_turn = models.IntegerField(default=0)
    iron_per_turn = models.IntegerField(default=0)
    silver = models.IntegerField(default=0)
    description = models.CharField(max_length=2000)