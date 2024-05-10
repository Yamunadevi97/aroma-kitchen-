# Create your models here.
from django.db import models
class cus(models.Model):
		name = models.CharField(max_length=25)
		place = models.CharField(max_length=100)
		ingredients = models.CharField(max_length=100)
		recipie = models.CharField(max_length=300)