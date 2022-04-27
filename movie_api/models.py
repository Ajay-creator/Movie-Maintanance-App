from tkinter import CASCADE
from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    release_date = models.DateField()
    votes = models.IntegerField(default=0, blank=True)

    class Meta:
        ordering = ['release_date']

    def __str__(self):
        return self.title


class Actor(models.Model):
    name = models.CharField(max_length=256)
    dob = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class MovieActorRelation(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.title + '/' + self.actor.name
