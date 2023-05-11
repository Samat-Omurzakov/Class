from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieListCreateAPIView.as_view()),
    path('api/v1/movies/<int:id>/', views.movie_detail_api_view),

    path('directors/', views.DirectorListAPIView.as_view()),
    path('directors/<int:pk>/', views.DirectorDetailAPIView.as_view()),

    path('genres/', views.GenreAPIViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('genres/<int:pk>', views.GenreAPIViewSet.as_view({
        'get': 'retrieve', 'post': 'update', 'delete': 'destroy'
    }))
]
