from rest_framework import serializers
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
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'title description duration director reviews rating'.split()
