from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField, IntegerField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateField()
    running_time = models.IntegerField()

    class Meta:
        db_table = "movies"


class Actor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField()
    movies = models.ManyToManyField(Movie, related_name='actors')

    class Meta:
        db_table = "actors"

