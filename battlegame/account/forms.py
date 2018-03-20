from django import forms
from django.contrib.auth.models import User
from servers.models import GameServer
from .models import Profile
from .appconfig import CLASS_CHOICES


# TODO: WHEN I USE THE CUSTOM MODEL MANAGER IN A FORM, LIKE BELOW I USE get_ids_and_names(), i cannot do makemigrations when i put a new field in the relative model
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    gameserver = forms.ChoiceField(choices=GameServer.objects.ids_and_names()) # comment out this and the other below to fix migrations issues. research the reason


class UserRegistrationForm(forms.ModelForm):
    gameserver = forms.ChoiceField(choices=GameServer.objects.ids_and_names())
    password = forms.CharField(label="Password", widget = forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget = forms.PasswordInput)
    tribe = forms.ChoiceField(choices=CLASS_CHOICES)
    capital_name = forms.CharField(label="name of capital")
    description = forms.CharField(label="Description", widget=forms.Textarea)

    class Meta:
        model = User
        fields = ("username", "first_name", "email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("passwords do not match")

        return cd["password"]

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {"first_name", "last_name", "email"}

class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ("tribe", "user")