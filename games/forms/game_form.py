from django.forms import ModelForm, widgets
from games.models import Games
from django import forms
from user.models import BuyerInfo, PaymentInfo

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
        model = BuyerInfo
        exclude = ['id']
        widgets = {
            'full_name': widgets.TextInput,
            'street_name': widgets.TextInput,
            'house_number': widgets.TextInput,
            'city': widgets.TextInput,
            'country': widgets.Select,
            'postal_code': widgets.TextInput,

        }

class PaymentForm(ModelForm):
    class Meta:
        model = PaymentInfo
        exclude = ['id']
        widgets = {
            'card_holder': widgets.TextInput,
            'card_number': widgets.TextInput,
            'card_exp': widgets.TextInput,
            'card_cvc': widgets.TextInput,
        }


