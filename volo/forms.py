from django import forms
from .models import Volo

class VoloForm(forms.ModelForm):
    class Meta:
        model = Volo
        fields = ('name', 'full_name', 'phone_number', 'town_or_city', 'content')