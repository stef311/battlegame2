from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def dashboard(request):
    return HttpResponse("dashboard here")

@login_required
def info(request):
    user = request.user
    user_tribe = user.profile.tribe
    context = {}
    context["tribe"] = user_tribe
    return render(request, "battle/info.html", context=context)

@login_required
def central_building(request):
    user = request.user # check later if this is required
    context = {}
    return render(request, "battle/central.html", context=context)

@login_required
def army_building(request):
    user = request.user # check later if this is required
    context = {}
    return render(request, "battle/army.html", context=context)

@login_required
def market_building(request):
    context = {}
    return render(request, "battle/market.html", context=context)