from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Movie, Actor, Review
from .serializers import MovieSerializer, MovieListSerializer, ActorListSerializer, ActorSerializer, ReviewListSerializer, ReviewSerializer

# Create your views here.
@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    serializer = MovieSerializer(movie)
    return Response(serializer.data)


# Create your views here.
@api_view(['GET'])
def actor_list(request):
  actors = Actor.objects.all()
  serializer = ActorListSerializer(actors, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def actor_detail(request, actor_pk):
  actor = Actor.objects.get(pk=actor_pk)
  serializer = ActorSerializer(actor)
  return Response(serializer.data)


# 전체 리뷰 목록 제공 함수
@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)



# 단일 리뷰 목록 제공  
@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, reviews_pk):
  review = Review.objects.get(pk=reviews_pk)
  if request.method == 'GET':
    serializer = ReviewSerializer(review)
    return Response(serializer.data)
  
  elif request.method == 'DELETE':
    review.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
  elif request.method == 'PUT':
     serializer = ReviewSerializer(review, data=request.data)
     if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


# 리뷰 생성
@api_view(['POST'])
def review_create(request, movie_pk):
  movie = Movie.objects.get(pk=movie_pk)
  serializer = ReviewSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    serializer.save(movie=movie)
    return Response(serializer.data, status=status.HTTP_201_CREATED)