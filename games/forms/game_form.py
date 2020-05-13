from django.forms import ModelForm, widgets
from games.models import Games
from django import forms
from user.models import UserInfo

class GameUpdateForm(ModelForm):
    class Meta:
        model = Games
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput,
            'description': widgets.TextInput,
            'category': widgets.Select,
            'on_sale': widgets.CheckboxInput
        }


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

class BuyGameForm(ModelForm):
    class Meta:
        model = UserInfo
        exclude = ['id']
        widgets = {
            'full_name': widgets.TextInput,
            'street_name': widgets.TextInput,
            'house_number': widgets.TextInput,
            'city': widgets.TextInput,
            'country': widgets.Select,
            'postal_code': widgets.TextInput,

        }