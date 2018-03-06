from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def overview(request):
    return HttpResponse("overview of all items on all your villages")


