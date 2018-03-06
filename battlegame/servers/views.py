from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def server_list(request):
    return HttpResponse("overview of all the servers")