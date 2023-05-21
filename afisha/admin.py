from django.contrib import admin
from afisha.models import Movie, Director, Genre, Review


# Register your models here.
# admin.site.register(Movie)
# admin.site.register(Director)
# admin.site.register(Genre)
# admin.site.register(Review)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'director', 'rating', 'duration', 'is_hit', 'created', 'updated')
    list_filter = ('name', 'director', 'rating', 'duration', 'is_hit', 'created', 'updated', 'genre')
    fields = ['name', 'director', 'rating', 'duration', 'is_hit', 'genre', 'description']


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'movie')

