from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import CreateVillageForm
from .models import Village, VillageBuildings, VillageItems, VillageUnits, VillageField
from battle.utils import calculate_attack_power

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
            new_village = Village.objects.create(user = request.user, wood=50, iron= 50, name=cd["name"], description=cd["description"])
            new_village.save()
            # initial troops to give to village
            if cd["type"] == "1": # add variables like these in settings
                warrior1 = 4
                warrior2 = 2
                warrior3 = 1
            elif cd["type"] == "2":
                warrior1 = 2
                warrior2 = 4
                warrior3 = 1
            else:
                warrior1 = 2
                warrior2 = 2
                warrior3 = 3
            print(cd["type"])

            new_village_units = VillageUnits.objects.create(village = new_village, warrior1 = warrior1,
                                                    warrior2=warrior2, warrior3=warrior3)


            new_village_items = VillageItems.objects.create(village = new_village, flag = 1) # Give one initial flag to village

            new_village_buildings = VillageBuildings.objects.create(village = new_village)

            for i in range(settings.WOOD_FIELDS_PER_VILLAGE):
                VillageField.objects.create(village=new_village, field_type=1)
            for i in range(settings.IRON_FIELDS_PER_VILLAGE):
                VillageField.objects.create(village=new_village, field_type=2)

            # Create an additional empty village field

            VillageField.objects.create(village=new_village, field_type=0) # 0 means neither wood nor iron

            return redirect("battle:overview")
        else:
            return HttpResponse("form not valid. please try with another name")
