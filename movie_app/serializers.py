from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Director, Movie, Review
from django.contrib.auth.models import User


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id username first_name last_name email'.split()


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name movie_count'.split()


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = 'title description duration director'.split()


class ReviewSerializer(serializers.ModelSerializer):
    author = UserSimpleSerializer()

    class Meta:
        model = Review
        fields = 'id author text stars'.split()


class MoviesReviewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = 'title description duration director rating'.split()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['reviews'] = ReviewSerializer(instance.reviews.all(), many=True,
                                                     context=self.context).data
        return representation




class DirectorValidSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    def validate_name(self, name):
        name_exists = Director.objects.filter(name=name).exists()
        if not name_exists:
            return name
        raise ValidationError('Director already exists!')


class MovieValidSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    duration = serializers.CharField(max_length=50)
    director_id = serializers.IntegerField()

    def validate_title(self, title):
        title_exists = Movie.objects.filter(title=title).exists()
        if not title_exists:
            return title
        raise ValidationError('Movie with this title already exists!')

    def validate_director_id(self, director_id):
        director_exists = Director.objects.filter(id=director_id).exists()
        if not director_exists:
            raise ValidationError('Director with this id already exists')
        return director_id


class ReviewValidSerializer(serializers.Serializer):
    author_id = serializers.IntegerField(default='Anonymous')
    text = serializers.CharField()
    movie_id = serializers.IntegerField()
    stars = serializers.IntegerField(default=0)
    def validate_movie_id(self, movie_id):
        movie_exists = Movie.objects.filter(id=movie_id).exists()
        if movie_exists:
            return movie_id
        raise ValidationError('Film with this id already exists!')