from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CreateGameServerForm
from .models import GameServer

# Create your views here.

def server_list(request):
    return HttpResponse("overview of all the servers")

@staff_member_required
def server_create(request):
    if request.method == "GET":
        create_gameserver_form = CreateGameServerForm()
        context = {}
        context.update({"create_gameserver_form": create_gameserver_form})
        return render(request, "servers/create.html", context=context)
    else:
        create_gameserver_form = CreateGameServerForm(request.POST)
        if create_gameserver_form.is_valid():
            return HttpResponse("POST method used")
        else:
            return HttpResponse("not valid")