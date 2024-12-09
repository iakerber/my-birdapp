from django import forms

from .models import Waterbird

class WaterbirdForm(forms.ModelForm):

    class Meta:
        model = Waterbird
        fields = ('name', 'back_color', 'breast_color', 'bill_size', 'leg_length', 'call_complexity', 'water_type', 'description')