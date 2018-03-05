from django.contrib import admin
from .models import Village

# Register your models here.

class VillageAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "attack_power", "defense_power", "population", "science", "culture"]

admin.site.register(Village, VillageAdmin)