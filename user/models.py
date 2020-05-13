import countries as countries
import datetime
from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField
from django import forms


# Create your models here.
from games.models import Games


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999)
    def __str__(self):
        return self.user.username

class BuyerInfo(models.Model):
    full_name = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    house_number = models.IntegerField()
    city = models.CharField(max_length=255)
    country = CountryField()
    postal_code = models.CharField(max_length=10)
    product = models.ForeignKey(Games, on_delete=models.CASCADE)

class PaymentInfo(models.Model):
    card_holder = models.CharField(max_length=255)
    card_number = models.CharField(max_length=16)
    card_exp = forms.DateField(widget=forms.SelectDateWidget)
    card_cvc = models.CharField(max_length=3)
    date_ordered = models.DateTimeField(auto_now=True)
    buyer_id = models.ForeignKey(BuyerInfo, on_delete=models.CASCADE)


