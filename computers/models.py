from django.db import models

# Create your models here.

class Computers(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    price = models.FloatField()
    on_sale = models.BooleanField()



# beint úr fyrirlestri 9
class ComputersImage(models.Model):
    image = models.CharField(max_length=999)
    computers_id = models.ForeignKey(Computers, on_delete=models.CASCADE)


