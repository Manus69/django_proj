from django.db import models
from django.contrib.auth.models import User

CF_LEN_MAX = 20

def rec_path(rec, filename):
    return f"img/{rec.pk}/{filename}"

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=CF_LEN_MAX)
    desc = models.TextField(null=False, blank=True)
    alg = models.TextField(null=False, blank=True)
    time = models.IntegerField(null=False, default=1)
    img = models.ImageField(null=True, blank=True, upload_to=rec_path)
    auth = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    
class Cat(models.Model):
    name = models.CharField(max_length=CF_LEN_MAX)
    recs = models.ManyToManyField(Recipe, related_name="category")