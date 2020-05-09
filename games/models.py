from django.db import models


class GamesCategory(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Games(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    category = models.ForeignKey(GamesCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    on_sale = models.BooleanField()
    def __str__(self):
        return self.name


#beint úr fyrirlestri 9
class GamesImage(models.Model):
    image = models.CharField(max_length=999)
    games = models.ForeignKey(Games, on_delete=models.CASCADE)
    def __str__(self):
        return self.image