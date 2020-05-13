import countries as countries
from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField

# Create your models here.
from games.models import Games


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999)
    def __str__(self):
        return self.user.username

class UserInfo(models.Model):
    full_name = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    house_number = models.IntegerField()
    city = models.CharField(max_length=255)
    country = CountryField()
    postal_code = models.CharField(max_length=10)


