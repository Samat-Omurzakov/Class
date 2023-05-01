from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from afisha.serializers import MovieSerializers, MovieValidateSerializer
from afisha.models import Movie


# Create your views here.

@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        data_dict = MovieSerializers(movies, many=True).data
        return Response(data=data_dict)
    elif request.method == "POST":
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors!': serializer.errors})
        name = serializer.validated_data.get('name')
        description = serializer.validated_data.get('description')
        is_hit = serializer.validated_data.get('is_hit')
        duration = serializer.validated_data.get('duration')
        rating = serializer.validated_data.get('rating')
        director_id = serializer.validated_data.get('director_id')
        genre = serializer.validated_data.get('genre')
        m_o = Movie.objects.create(name=name, description=description, is_hit=is_hit, duration=duration, rating=rating,
                                   director_id=director_id)
        m_o.genre.set(genre)
        m_o.save()
        return Response(data=MovieSerializers(m_o).data)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'errors': 'Movie not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data_dict = MovieSerializers(movie, many=False).data
        return Response(data=data_dict)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie.name = serializer.validated_data.get('name')
        movie.description = serializer.validated_data.get('description')
        movie.duration = serializer.validated_data.get('duration ')
        movie.is_hit = serializer.validated_data.get('is_hit')
        movie.rating = serializer.validated_data.get('rating ')
        movie.director_id = serializer.validated_data.get('director_id')
        movie.genre.set(request.data.get('genre'))
        movie.save()
        return Response(data=MovieSerializers(movie).data,
                        status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def test_api_view(request):
    data_dict = {
        'test': 'Hello World!',
        'int': 123,
        'bool': True,
        'dict': {'key': 'value'},
        'list': [1, 2, 3]
    }
    return Response(data=data_dict)
