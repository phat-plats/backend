from django.db import models

class InsecureUser(models.Model):
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=80) # UNHASHED PASSWORD NOT SECURE
    def __str__(self):
        return self.username

class Product(models.Model):
    name = models.CharField(max_length=140)
    searchName = models.CharField(max_length=140, null=True, blank=True)
    upc = models.CharField(max_length=16)
    imageUrl = models.CharField(max_length=1024, default="https://placeholdit.imgix.net/~text?txtsize=19&txt=200%C3%97300&w=200&h=300")
    recyclingType = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name

class Comment(models.Model):
    contents = models.CharField(max_length=140)
    poster = models.CharField(max_length=80)
    score = models.IntegerField(default=0)
    product = models.ForeignKey(Product)
    def __str__(self):
        return self.poster + " | " + self.product.name

class HazMat(models.Model):
    material = models.CharField(max_length=140)
    product = models.ForeignKey(Product, related_name="hazmats")
    def __str__(self):
        return self.material
# Create your models here.
