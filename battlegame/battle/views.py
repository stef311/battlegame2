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
