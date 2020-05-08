from django.forms import ModelForm, widgets
from games.models import Games
from django import forms

class GameCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput)
    class Meta:
        model = Games
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput,
            'description': widgets.TextInput,
            'category': widgets.Select,
            'on_sale': widgets.CheckboxInput
        }
