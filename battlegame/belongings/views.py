from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def overview(request):
    return HttpResponse("overview of all items on all your villages")

@login_required
def market(request):
    return HttpResponse("market building here. exchange resources. buy items")

@login_required
def resource_exchange(request):
    return HttpResponse("user can redirect here from market and warehouse too. can exchange resources")

@login_required
def warehouse(request):
    return HttpResponse("warehouse building here. exchange resources. here you can see all your resources and how much you earn per turn")




