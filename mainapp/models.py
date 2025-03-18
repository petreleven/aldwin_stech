from django.db import models

# Create your models here.
class Player(models.Model):
    username = models.CharField(max_length= 20)
    password = models.CharField(max_length= 50)
    profile_pic = models.ImageField()

class Resource(models.Model):
    username = models.CharField(max_length= 6)
    points = models.IntegerField()

class Movie(models.Model):
    Name = models.CharField(max_length= 14)
    Description = models.TextField()

