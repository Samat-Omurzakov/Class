from django.contrib import admin
from afisha.models import Movie, Director, Genre, Review

# Register your models here.
admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Review)