from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def all(request):
    return HttpResponse("all villages")

@login_required #make it so that it needs to be the village owner, else redirect to different page
def main(request, village_id):
    return HttpResponse(village_id)

