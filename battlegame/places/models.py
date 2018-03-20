from django.db import models
from servers.models import GameServer

# Create your models here.

class Tile(models.Model): # TODO: write a check to see if tile is going to be put on top of another and overwrite it
    gameserver = models.ForeignKey(GameServer, on_delete=models.CASCADE)
    coordinateX = models.IntegerField(null=False, blank=False)
    coordinateY = models.IntegerField(null=False, blank=False)


class Place(Tile):
    is_buildable = models.BooleanField(default=True)
    warrior1 = models.IntegerField(default=0)
    warrior2 = models.IntegerField(default=0)
    warrior3 = models.IntegerField(default=0)
    wood = models.IntegerField(default=0)
    iron = models.IntegerField(default=0)
    culture = models.IntegerField(default=0)
    science = models.IntegerField(default=0)
    silver = models.IntegerField(default=0)