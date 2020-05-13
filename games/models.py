from django.db import models
from django.conf import settings
from computers.models import Computers
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

   # slug = models.SlugField()
    #quantity = models.IntegerField(default=1)
    def __str__(self):
        return self.name

  #  def get_absolute_url(self):
  #     return reverse("games:games", kwargs={
    #        'slug': self.slug
     #   })

class GamesImage(models.Model):
    image = models.CharField(max_length=999)
    games = models.ForeignKey(Games, on_delete=models.CASCADE)
    def __str__(self):
        return self.image

class OrderItem(models.Model):
    items = models.ForeignKey(Games, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)


