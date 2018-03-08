import os, sys

# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "battlegame.settings")

# This is so models get loaded.

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from servers.models import GameServer
from django.contrib.auth.models import User

for server in GameServer.objects.all():
    server.delete()
