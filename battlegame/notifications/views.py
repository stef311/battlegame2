from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def message_list(request):
    return HttpResponse("message list here")

@login_required
def notification_list(request):
    return HttpResponse("notification list here")