from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from servers.models import GameServer
# Create your views here.

@login_required
def dashboard(request):
    return HttpResponse("dashboard here")

@login_required
def overview(request):

    if request.session.get("gameserver") == None:
        return HttpResponse("login first")
    else:
        gameserver = request.session["gameserver"]
        user = request.user
        user_tribe = user.profile.tribe
        user_villages = user.villages.all()
        context = {}
        context["tribe"] = user_tribe
        context["user_villages"] = user_villages
        return render(request, "battle/overview.html", context=context)

@login_required
def army(request):
    user = request.user
    return HttpResponse("army building here. user can see their troops and also train more. can also see heroes")


