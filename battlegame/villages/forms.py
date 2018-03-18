
from django import forms
from .models import Village
from .appconfig import VILLAGE_TYPE_CHOICES

class CreateVillageForm(forms.Form):
    name = forms.CharField(label="village name", max_length=20)
    type = forms.ChoiceField(label="village type", choices=VILLAGE_TYPE_CHOICES, widget=forms.Select,required=True)
