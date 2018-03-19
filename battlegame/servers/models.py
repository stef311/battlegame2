from django.db import models
from django.conf import settings
from .appconfig import TASK_TYPES
from battle.models import Unit

# Create your models here.

class GameServerManager(models.Manager):
    def ids_and_names(self):
        gameservers = GameServer.objects.all()
        pairs = []
        for g in gameservers:
            pair = (g.id, g.name)
            pairs.append(pair)
        return pairs


class GameServer(models.Model):
    name = models.CharField(max_length=20)
    turn = models.IntegerField(default=0)
    password = models.CharField(max_length=20)  
    description = models.TextField(max_length=20)
    players_allowed = models.IntegerField(default=0)
    players = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="gameservers")
    players_finished_turn = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="gameservers_finished_turn") # then(on change) check to see if same as players length to end turns

    objects = GameServerManager()

    def __str__(self):
        return self.name

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
