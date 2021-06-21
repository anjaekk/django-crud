from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=128)
    age = models.IntegerField()

    class Meta:
        db_table = "owners"

class Dog(models.Model):
    owner = models.ForeignKey('Owner', on_delete=CASCADE)
    name = models.CharField(max_length=30)
    age = IntegerField()

    class Meta:
        db_table = "dogs"




