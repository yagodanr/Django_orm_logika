from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    
class Game(models.Model):
    name = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
