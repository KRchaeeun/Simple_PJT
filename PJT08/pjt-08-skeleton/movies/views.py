from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe
from .models import Movie, Genre
from django.http import JsonResponse
import random

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    genres = Genre.objects.all()
    context = {
        'genres' : genres
    }
    return render(request, 'movies/recommended.html', context)

@require_safe
def recommended_gen(request, gen_pk):
    matching_movies = Movie.objects.filter(genres=gen_pk)
    
    if matching_movies.count() == 0:
        return JsonResponse({"message": "Not enough matching movies."}, status=400)
    
    recommended_movies_data = []
    for recommended_movies in random.sample(list(matching_movies), min(3, matching_movies.count())):
        genres_list = [genre.name for genre in recommended_movies.genres.all()]
        movie_data = {
            'pk': recommended_movies.pk,
            'title' : recommended_movies.title,
            'release_date' : recommended_movies.release_date,
            'vote_average' : recommended_movies.vote_average,
            'overview' : recommended_movies.overview,
            'poster_path' : recommended_movies.poster_path,
            'genres' : genres_list,
        }
        recommended_movies_data.append(movie_data)

    return JsonResponse(recommended_movies_data, safe=False)
