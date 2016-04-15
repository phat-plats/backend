from django.db import models

class InsecureUser(models.Model):
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=80) # UNHASHED PASSWORD NOT SECURE

class Product(models.Model):
    name = models.CharField(max_length=140)
    upc = models.CharField(max_length=16)
    imageUrl = models.CharField(max_length=1024, default="http://placehold.it/350x150")
    recyclingType = models.IntegerField(null=True, blank=True)

class Comment(models.Model):
    contents = models.CharField(max_length=140)
    poster = models.CharField(max_length=80)
    score = models.IntegerField(default=0)
    product = models.ForeignKey(Product)

class HazMat(models.Model):
    material = models.CharField(max_length=140)
    product = models.ForeignKey(Product)
# Create your models here.
