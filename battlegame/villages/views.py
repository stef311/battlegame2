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
            new_village = Village.objects.create(user = request.user, name=cd["name"], description=cd["description"])
            new_village.save()
            # initial troops to give to village
            if cd["type"] == "1": # add variables like these in settings
                offensive_units = 4
                defensive_units = 2
                neutral_units = 1
            elif cd["type"] == "2":
                offensive_units = 2
                defensive_units = 4
                neutral_units = 1
            else:
                offensive_units = 2
                defensive_units = 2
                neutral_units = 3
            print(cd["type"])

            new_village_units = VillageUnits.objects.create(village = new_village, warrior1 = offensive_units,
                                                    warrior2=defensive_units, warrior3=neutral_units)

            # new_village.attack_power += calculate_attack_power(offensive_units, defensive_units, neutral_units)

            new_village_items = VillageItems.objects.create(village = new_village, flag = 1)

            new_village_buildings = VillageBuildings.objects.create(village = new_village)

            for i in range(settings.WOOD_FIELDS_PER_VILLAGE):
                VillageField.objects.create(village=new_village, field_type=1)
                new_village.wood_per_turn += 10 # each field produces 10 per turn
            for i in range(settings.IRON_FIELDS_PER_VILLAGE):
                VillageField.objects.create(village=new_village, field_type=2)
                new_village.iron_per_turn += 10

            # Create an additional empty village field
            new_village.save()

            VillageField.objects.create(village=new_village, field_type=0) # 0 means neither wood nor iron

            return redirect("battle:overview")
        else:
            return HttpResponse("form not valid. please try with another name")
