from rest_framework import serializers
from .models import Movie, Actor, Review

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview',)


# 전체 리뷰 목록 Serializer
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content',)


class MovieSerializer(serializers.ModelSerializer):
  class ActorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('name',)
  
  actors = ActorNameSerializer(many = True, read_only=True)
  review_set = ReviewListSerializer(many=True, read_only=True)


  class Meta:
      model = Movie
      fields = '__all__'

class ActorListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Actor
    fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
  class MovieTitleSerializer(serializers.ModelSerializer):
    class Meta:
      model = Movie
      fields = ('title',)
  
  movie = MovieTitleSerializer(many=True, read_only=True)

  class Meta:
    model = Actor
    fields = ('id', 'name', 'movie',)


# 단일 리뷰 목록 Serializer  
class ReviewSerializer(serializers.ModelSerializer):
  class MovieTitleSerializer(serializers.ModelSerializer):
    class Meta:
      model = Movie
      fields = ('title',)
  
  movie = MovieTitleSerializer(read_only=True)

  class Meta:
    model = Review
    fields = ('id', 'movie', 'title', 'content',)
    read_only_fields = ('id', 'movie',)  # 유효성 검사에서 제외시키고 데이터 조회 시에는 출력하도록