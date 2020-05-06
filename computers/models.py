from django.db import models

# Create your models here.
class ComputersCategory(models.Model):
    name = models.CharField(max_length=255)


class Computers(models.Model):
    name = models.CharField(max_length=255)
    description = model.CharField(max_length=999, blank=True)
    category = models.ForeignKey(ComputersCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    on_sale = models.BooleanField()



# beint úr fyrirlestri 9
class ComputersImage(models.Model):
    image = models.CharField(max_length=999)
    game = models.ForeignKey(Computers, on_delete=models.CASCADE)
