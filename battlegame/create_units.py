import os, sys

# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "battlegame.settings")

# This is so models get loaded.

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from battle.models import Unit

#First delete
for unit in Unit.objects.all():
    unit.delete()

#Now create
Unit.objects.create(name="warrior1",
                    attack_power=4,
                    defence_power=2,
                    speed=1,
                    population=1,
                    culture=0,
                    science=0,
                    wood=0,
                    iron=0,
                    wood_per_turn=0,
                    iron_per_turn=0,
                    silver=0,
                    description="offensive warrior")

Unit.objects.create(name="warrior2",
                    attack_power=2,
                    defence_power=4,
                    speed=1,
                    population=1,
                    culture=0,
                    science=0,
                    wood=0,
                    iron=0,
                    wood_per_turn=0,
                    iron_per_turn=0,
                    silver=0,
                    description="defensive warrior")

Unit.objects.create(name="warrior3",
                    attack_power=3,
                    defence_power=3,
                    speed=1,
                    population=1,
                    culture=0,
                    science=0,
                    wood=0,
                    iron=0,
                    wood_per_turn=0,
                    iron_per_turn=0,
                    silver=0,
                    description="neutral warrior")

