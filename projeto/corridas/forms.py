from django import forms
from corridas.models import Corridas

class CorridasForm(forms.ModelForm):
    class Meta:
        model = Corridas