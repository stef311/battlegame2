from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def overview(request):
    return HttpResponse("overview of all items on all your villages")

@login_required
def academy(request, village_id):
    return HttpResponse("academy building here.")

@login_required
def museum(request, village_id): #test if village_id needs to be the same name with the parameter in the url(regex)
    return HttpResponse(str(village_id))



