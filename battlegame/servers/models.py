from django.db import models

# Create your models here.

class GameServer(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    players_allowed = models.IntegerField(default=0)
    players_registered = models.IntegerField(default=0)