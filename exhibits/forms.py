from django import forms
from .models import Exhibit, ExhibitItem

class ExhibitForm(forms.ModelForm):
    class Meta:
        model = Exhibit
        fields = ['name', 'description', 'floor', 'is_open']

class ExhibitItemForm(forms.ModelForm):
    class Meta:
        model = ExhibitItem
        fields = ['exhibit', 'name', 'description', 'image', 'status']
