from django.db import models
from django.conf import settings
from .appconfig import TASK_TYPES
from battle.models import Unit

# Create your models here.

class GameServer(models.Model):
    name = models.CharField(max_length=20)
    turn = models.IntegerField(default=0)
    password = models.CharField(max_length=20)  
    description = models.TextField(max_length=20)
    players_allowed = models.IntegerField(default=0)
    players = models.ManyToManyField(settings.AUTH_USER_MODEL)


class OneTimeTask(models.Model):
    server = models.ForeignKey(GameServer, on_delete=models.CASCADE)
    turn = models.IntegerField(default=0)

    class Meta:
        abstract=True


class ContinuousTask(models.Model): # something like a buff
    server = models.ForeignKey(GameServer, on_delete=models.CASCADE)
    turn_begin = models.IntegerField(default=0)
    turn_end = models.IntegerField(default=0)

    class Meta:
        abstract=True


class AttackTask(OneTimeTask):
    attack_power = models.IntegerField(default=0)
    defence_power = models.IntegerField(default=0)
    defensive_traps = models.IntegerField(default=0)


class BuildingTask(OneTimeTask):
    building_name = models.IntegerField(default=0)
    levels_to_upgrade = models.IntegerField(default=0)
