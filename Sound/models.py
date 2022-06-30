from django.db import models

# Create your models here.

# This is the generic class for an item that can be gutiar, electric, bass or other
class Item(models.Model):
    # name of the item
    name = models.CharField(max_length=100)
    # -1 = default null instrument: will not be displayed
    # 0-5 are normal instrument types
    type = models.IntegerField(default=-1)
    # price of the item
    price = models.FloatField(default=0)
    # color of item
    color = models.CharField(max_length=100)
    # top wood type
    top_wood = models.CharField(max_length=100)
    # back wood type
    back_wood = models.CharField(max_length=100)
    # has electronics?
    has_electronics = models.BooleanField(default=0)
    # short description
    short_description = models.TextField()
    # number of string
    num_of_strings = models.IntegerField()
    # brand
    brand = models.CharField(max_length=100)


