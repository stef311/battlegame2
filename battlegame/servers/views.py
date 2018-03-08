from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

def server_list(request):
    return HttpResponse("overview of all the servers")

@staff_member_required
def server_create(request):
    return HttpResponse("Only staff can access this page")