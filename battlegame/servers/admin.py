from django.contrib import admin
from .models import GameServer

# Register your models here.
class GameServerAdmin(admin.ModelAdmin):
    list_display = ["name", "players_allowed"]

admin.site.register(GameServer, GameServerAdmin)