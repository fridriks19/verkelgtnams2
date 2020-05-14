from django.db import models
from django.conf import settings
from computers.models import Computers, Manufacturer
from django.shortcuts import reverse

class GamesCategory(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Games(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    category = models.ForeignKey(GamesCategory, on_delete=models.CASCADE)
    console = models.ForeignKey(Computers, on_delete=models.CASCADE)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    on_sale = models.BooleanField()
    def __str__(self):
        return self.name


class GamesImage(models.Model):
    image = models.CharField(max_length=999)
    games = models.ForeignKey(Games, on_delete=models.CASCADE)
    def __str__(self):
        return self.image

