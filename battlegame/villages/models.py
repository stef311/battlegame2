from django.db import models
from django.conf import settings

# Create your models here.

class Village(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="villages")
    server = models.IntegerField(default=0) # suppose 0 is the NULL server. for testing only
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

class VillageUnits(models.Model):
    village = models.OneToOneField("Village", on_delete=models.CASCADE)
    warrior1 = models.IntegerField(default=0)
    warrior2 = models.IntegerField(default=0)
    warrior3 = models.IntegerField(default=0)

class VillageBuildings(models.Model):
    village = models.OneToOneField("Village", on_delete=models.CASCADE)
    army = models.IntegerField(default=0)
    market = models.IntegerField(default=0)
    academy = models.IntegerField(default=0)
    museum = models.IntegerField(default=0)

class VillageItems(models.Model):
    flag = models.IntegerField(default=0)


