from django.db import models
from django.conf import settings
from .appconfig import TASK_TYPES

# Create your models here.

class GameServer(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    description = models.TextField(max_length=20)
    players_allowed = models.IntegerField(default=0)
    players = models.ManyToManyField(settings.AUTH_USER_MODEL)

class OneTimeTask(models.Model):
    server = models.ForeignKey(GameServer, on_delete=models.CASCADE)
    task_type = models.IntegerField(choices=TASK_TYPES,default=0)
    players = models.ManyToManyField(settings.AUTH_USER_MODEL)
    
    building = models.CharField(max_length=20)


class DurationAction(models.Model):
