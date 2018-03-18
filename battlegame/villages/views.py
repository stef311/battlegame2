from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CreateVillageForm

# Create your views here.

@login_required
def all(request):
    return HttpResponse("all villages")

@login_required #make it so that it needs to be the village owner, else redirect to different page
def main(request, village_id):
    return HttpResponse(village_id)

@login_required
def create(request):
    context = {}
    if request.method == "GET":
        create_form = CreateVillageForm()
        context.update({"create_form":create_form})

    return render(request, "villages/create.html", context=context)