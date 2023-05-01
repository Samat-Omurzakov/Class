from django.db import models


# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True, blank=True)
    genre = models.ManyToManyField(Genre, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    rating = models.FloatField()
    duration = models.IntegerField()
    is_hit = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def director_name(self):
        if self.director:
            return self.director.name
        return 'NO director'


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_review')

    def __str__(self):
        return self.text
