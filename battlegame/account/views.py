from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.conf import settings
from .forms import UserRegistrationForm, UserLoginForm


# Create your views here.

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()

            return redirect("account:user_login")
        else:
            return HttpResponse("Form not valid")
    else:
        registration_enabled = settings.REGISTRATION_ENABLED

        if registration_enabled:
            user_form = UserRegistrationForm()
            context = {"user_form": user_form}
            return render(request, "account/register.html", context=context)
        else:
            context = {}
            return render(request, "account/registration_disabled.html", context=context)

def user_login(request):
    if request.method == "POST":
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            user = authenticate(username=cd["username"],
                                password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("account:register")
                else:
                    return HttpResponse("user is not active")
            else:
                return HttpResponse("Invalid Login")
        else:
            return HttpResponse("Not valid form")
    else:
        user_form = UserLoginForm()
        context = {"user_form": user_form}
        return render(request, "account/login.html", context=context)