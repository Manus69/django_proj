from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField(null=False, blank=True)
    alg = models.TextField(null=False, blank=True)
    time = models.IntegerField(null=False)
    img = models.ImageField()
    auth = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Cat(models.Model):
    name = models.CharField(max_length=20)