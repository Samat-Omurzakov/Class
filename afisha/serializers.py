from rest_framework import serializers
from afisha.models import Movie, Director, Genre, Review
from rest_framework.validators import ValidationError


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text'.split()


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializers(serializers.ModelSerializer):
    director = DirectorSerializers()
    genre = GenreSerializers(many=True)
    genre_list = serializers.SerializerMethodField()
    movie_review = ReviewSerializers(many=True)

    class Meta:
        model = Movie
        fields = 'id movie_review name director director_name genre genre_list'.split()

    def get_genre_list(self, movie):
        return [genre.name for genre in movie.genre.all()]


class MovieValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=1, max_length=10)
    description = serializers.CharField(required=False)
    is_hit = serializers.BooleanField()
    rating = serializers.FloatField(min_value=1, max_value=10)
    director_id = serializers.IntegerField()
    genre = serializers.ListField(child=serializers.IntegerField())
    duration = serializers.IntegerField()

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('Director does not exist!!!')
        return director_id

    def validate_genre(self, genre):
        g = Genre.objects.filter(id__in=genre).values_list('id', flat=True)
        if len(g) != len(genre):
            raise ValidationError('genre does not exist!!!')
        return genre
