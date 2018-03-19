from django.db import models
from django.utils import timezone
from django.conf import settings
from .appconfig import FIELD_TYPES
from battle.models import Unit
from battle.utils import calculate_attack_power, calculate_defence_power, calculate_population
from .utils import calculate_resources_per_turn

# Create your models here.

class Village(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="villages")
    gameserver = models.IntegerField(default=0) # suppose 0 is the NULL server. for testing only
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

class VillageUnitsManager(models.Manager):
    def create(self, *args, **kwargs): # do the same for update
        obj = self.model(**kwargs)
        overall_attack = calculate_attack_power(obj.warrior1, obj.warrior2, obj.warrior3)
        overall_defence = calculate_defence_power(obj.warrior1, obj.warrior2, obj.warrior3)
        overall_population = calculate_population(obj.warrior1, obj.warrior2, obj.warrior3)

        obj.village.attack_power += overall_attack
        obj.village.defence_power += overall_defence
        obj.village.population += overall_population

        obj.village.save()

        self._for_write = True
        obj.save(force_insert=True, using=self.db)
        return obj

class VillageUnits(models.Model):
    village = models.OneToOneField("Village", on_delete=models.CASCADE)
    warrior1 = models.IntegerField(default=0) #offensive
    warrior2 = models.IntegerField(default=0) #defensive
    warrior3 = models.IntegerField(default=0) #neutral

    objects = VillageUnitsManager()


class VillageBuildings(models.Model):
    village = models.OneToOneField("Village", on_delete=models.CASCADE)
    army = models.IntegerField(default=1)
    market = models.IntegerField(default=1)
    academy = models.IntegerField(default=1)
    museum = models.IntegerField(default=1)


class VillageItems(models.Model):
    village = models.OneToOneField("Village", on_delete=models.CASCADE)
    flag = models.IntegerField(default=0)


class VillageFieldManager(models.Manager):
    def create(self, *args, **kwargs):
        obj = self.model(**kwargs)

        wood_per_turn, iron_per_turn = calculate_resources_per_turn(obj.field_type)

        obj.village.wood_per_turn += wood_per_turn
        obj.village.iron_per_turn += iron_per_turn
        obj.village.save()

        self._for_write = True
        obj.save(force_insert=True, using=self.db)
        return obj

class VillageField(models.Model):
    village = models.ForeignKey(Village, related_name="fields", on_delete=models.CASCADE)
    field_type = models.IntegerField(choices=FIELD_TYPES, default=1)
    level = models.IntegerField(default=1)

    objects = VillageFieldManager()
