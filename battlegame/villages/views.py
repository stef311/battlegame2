from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CreateVillageForm
from .models import Village, VillageBuildings, VillageItems, VillageUnits

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

    else :
        create_form = CreateVillageForm(request.POST)
        if create_form.is_valid():
            cd = create_form.cleaned_data
            new_village = Village.objects.create(user = request.user, name=cd["name"], description=cd["description"])
            new_village.save()
            # initial troops to give to village
            return redirect("battle:overview")
        else:
            return HttpResponse("form not valid. please try with another name")
