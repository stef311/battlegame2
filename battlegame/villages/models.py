from django.db import models
from django.utils import timezone
from django.conf import settings
from .appconfig import FIELD_TYPES
# Create your models here.

class Village(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="villages")
    server = models.IntegerField(default=0) # suppose 0 is the NULL server. for testing only
    name = models.CharField(max_length=20)
    attack_power = models.IntegerField(default=0)
    defence_power = models.IntegerField(default=0)
    population = models.IntegerField(default=0)
    culture = models.IntegerField(default=0)
    science = models.IntegerField(default=0)
    wood = models.IntegerField(default=0)
    iron = models.IntegerField(default=0)
    culture_per_turn = models.IntegerField(default=0)
    science_per_turn = models.IntegerField(default=0)
    wood_per_turn = models.IntegerField(default=0)
    iron_per_turn = models.IntegerField(default=0)
    silver = models.IntegerField(default=0)
    description = models.CharField(max_length=2000)
    date_created = models.DateTimeField(default=timezone.now, blank=True, null=True)

class VillageUnits(models.Model):
    village = models.OneToOneField("Village", on_delete=models.CASCADE)
    warrior1 = models.IntegerField(default=0) #offensive
    warrior2 = models.IntegerField(default=0) #defensive
    warrior3 = models.IntegerField(default=0) #neutral

class VillageBuildings(models.Model):
    village = models.OneToOneField("Village", on_delete=models.CASCADE)
    army = models.IntegerField(default=1)
    market = models.IntegerField(default=1)
    academy = models.IntegerField(default=1)
    museum = models.IntegerField(default=1)

class VillageItems(models.Model):
    village = models.OneToOneField("Village", on_delete=models.CASCADE)
    flag = models.IntegerField(default=0)

class VillageField(models.Model):
    village = models.ForeignKey(Village, related_name="fields", on_delete=models.CASCADE)
    field_type = models.IntegerField(choices=FIELD_TYPES, default=1)
    level = models.IntegerField(default=1)
