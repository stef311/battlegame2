from django.db import models
from django.utils import timezone
from django.conf import settings
from servers.models import GameServer
from .appconfig import NOTIFICATION_TYPES

# Create your models here.

class Message(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=1000)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="sent", on_delete=models.DO_NOTHING) #TODO change this DO_NOTHING.problem is when user is registered with username/id of user that existed in the past
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="received", on_delete=models.DO_NOTHING)
    datetime_created = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    server = models.ForeignKey(GameServer, on_delete=models.CASCADE)

class Notification(models.Model):
    notification_type = models.IntegerField(choices=NOTIFICATION_TYPES, default=3)
    body = models.TextField(max_length=1000)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    server = models.ForeignKey(GameServer, on_delete=models.CASCADE)



