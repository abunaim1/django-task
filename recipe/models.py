from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)