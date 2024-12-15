from django import forms

from .models import Waterbird, Raptor, Songbird


class WaterbirdForm(forms.ModelForm):

    class Meta:
        model = Waterbird
        fields = ('name', 'back_color', 'breast_color', 'bill_size', 'leg_length', 'call_complexity', 'water_type', 'description', 'image_bird')


class RaptorForm(forms.ModelForm):

    class Meta:
        model = Raptor
        fields = ('name', 'description', 'image_bird',)


class SongbirdForm(forms.ModelForm):

    class Meta:
        model = Songbird
        fields = ('name', 'description', 'image_bird',)