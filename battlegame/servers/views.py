from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

from .forms import CreateGameServerForm, JoinGameServerForm
from .models import GameServer

# Create your views here.

def server_list(request):
    gameservers = GameServer.objects.all()
    context = {}
    context.update({"gameservers": gameservers})
    if request.user.is_authenticated:
        context.update({"gameservers_joined": request.user.gameservers})
    return render(request, "servers/list.html", context=context)

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
            cd = create_gameserver_form.cleaned_data
            name = cd["name"]
            description = cd["description"]
            password = cd["password"]
            players_allowed = cd["players_allowed"]
            new_gameserver, created = GameServer.objects.get_or_create(name=name, description=description,
                                                                       password=password,players_allowed=players_allowed)
            if created:
                return HttpResponse("server created")
            else:
                return HttpResponse("server with this name already exists")
            # new_gameserver = create_gameserver_form.save(commit=False)
            # # new_gameserver.set_password(create_gameserver_form.cleaned_data["password"]) #TODO: create something like this that works
            # new_gameserver.save()
            # return HttpResponse("POST method used")
        else:
            return HttpResponse("not valid")

@login_required
def server_detail(request, server_id):
    server = GameServer.objects.get(id=server_id)
    if request.method == "GET":
        players_registered = server.players.all()
        join_gameserver_form = JoinGameServerForm()
        context = {}
        context.update({"players_registered": players_registered})
        context.update({"join_gameserver_form": join_gameserver_form})
        return render(request,"servers/detail.html", context=context)
    else:
        join_gameserver_form = JoinGameServerForm(request.POST)
        if join_gameserver_form.is_valid():
            cd = join_gameserver_form.cleaned_data
            if server.password == cd["password"]:
                print(request.user)
                server.players.add(request.user)
                server.save()
                return HttpResponse("password is correct")
            else:
                return HttpResponse("password not correct")
        else:
            return HttpResponse("form not valid")