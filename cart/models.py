from django.db import models
from games.models import Games
from __future__ import unicode_literals

# Create your models here.
from user.models import Profile


class OrderItem(models.Model):
    games = models.OneToOneField(Games, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(defult=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)
    def __str__(self):
        return self.games.name

class Order(models.Model):
    itm_num = models.CharField(max_length=15)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(defult=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.itm_num)