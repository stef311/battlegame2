from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm, ProfileEditForm, UserEditForm
from .models import Profile
from villages.models import Village # why is it red on pycharm
from servers.models import GameServer


# Create your views here.

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            cd = user_form.cleaned_data

            new_user = user_form.save(commit=False)
            new_user.set_password(cd["password"])
            new_user.save()
            profile = Profile.objects.create(user=new_user,
                                             tribe=cd["tribe"],
                                             description=cd["description"])
            profile.save()
            capital = Village.objects.create(user=new_user, name=cd["capital_name"])
            capital.save()

            GameServer.objects.get(id = cd["gameserver"]).players.add(new_user)
            messages.add_message(request, messages.INFO, "You registered successfully and can now login")

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
    context = {}
    if request.method == "POST":
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            user = authenticate(username=cd["username"],
                                password=cd["password"])

            gameserver = cd["gameserver"]
            context.update({"gameserver": gameserver})
            if user is not None:
                if user.is_active:
                    if user in GameServer.objects.get(id=gameserver).players.all():
                        request.session["gameserver"] = gameserver # TODO: erase it in logout
                        login(request, user)

                        #TODO: implement 'next' feature. get next from url and redirect there
                        return redirect("battle:overview")
                    else:
                        return HttpResponse("Not registered in this server. Please register first from the server list")
                else:
                    return HttpResponse("user is not active")
            else:
                return HttpResponse("Invalid Login")
        else:
            return HttpResponse("Not valid form")
    else:
        user_form = UserLoginForm()
        context.update({"user_form": user_form})
        return render(request, "account/login.html", context=context)

@login_required
def user_logout(request):
    logout(request)
    messages.add_message(request, messages.INFO, "You successfully logged out")
    return redirect("account:user_login")

@login_required
def edit_profile(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("battle:dashboard")
        else:
            return HttpResponse("form not valid")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, "account/edit.html", {"user_form": user_form, "profile_form": profile_form})
