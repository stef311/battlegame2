from django.forms import ModelForm
from .models import GameServer
from django import forms

class CreateGameServerForm(ModelForm):
    password = forms.CharField(label="Password", widget = forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget = forms.PasswordInput)

    class Meta:
        model = GameServer
        fields = ["name", "description", "players_allowed"]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("passwords do not match")

        return cd["password"]

    def clean_players_allowed(self):
        cd = self.cleaned_data
        if cd["players_allowed"] > 8:
            raise forms.ValidationError("cannot allow more than 8 players")

        return cd["players_allowed"]

class JoinGameServerForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
