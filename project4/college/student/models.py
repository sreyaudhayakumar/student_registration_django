from django.db import models

# Create your models here.
class Person(models.Model):
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.IntegerField()
    place = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    course = models.CharField(max_length=100)
    email = models.EmailField()
    photo = models.FileField()