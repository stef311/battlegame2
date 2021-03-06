
from django import forms
from .models import Village
from .appconfig import VILLAGE_TYPE_CHOICES

class CreateVillageForm(forms.Form):
    name = forms.CharField(label="village name", max_length=20)
    type = forms.ChoiceField(label="village type", choices=VILLAGE_TYPE_CHOICES, widget=forms.Select,required=True)
    description = forms.CharField(label="village description", max_length=200, widget=forms.Textarea)

    def clean_name(self):
        cd = self.cleaned_data
        name = cd["name"]
        if Village.objects.all().filter(name=name).exists():
            raise forms.ValidationError("Village with that name already exists")
        return name