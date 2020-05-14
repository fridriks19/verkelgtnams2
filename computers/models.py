from django.db import models

# Create your models here.

class Computers(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    price = models.FloatField()
    on_sale = models.BooleanField()
    discount_price = models.FloatField(blank=True, null=True)
    def __str__(self):
        return self.name


class ComputersImage(models.Model):
    image = models.CharField(max_length=999)
    image2 = models.CharField(max_length=999)
    computers = models.ForeignKey(Computers, on_delete=models.CASCADE)
    def __str__(self):
        return self.image

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    year_of_start = models.DateTimeField()



