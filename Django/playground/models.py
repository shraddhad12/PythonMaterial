from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=25)
    users = models.ManyToManyField(User)

# Create your models here.
