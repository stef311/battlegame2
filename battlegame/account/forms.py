from django import forms
from django.contrib.auth.models import User
from .models import Profile
from .appconfig import CLASS_CHOICES

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget = forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget = forms.PasswordInput)
    tribe = forms.ChoiceField(choices=CLASS_CHOICES)
    description = forms.CharField(label="Description", widget=forms.Textarea)

    class Meta:
        model = User
        fields = ("username", "first_name", "email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidatioError("passwords do not match")

        return cd["password"]


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ()