from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from games.models import Games


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999)

    def __str__(self):
        return self.user.username

