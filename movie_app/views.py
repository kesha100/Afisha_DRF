from rest_framework import status, request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializers import *
from rest_framework import generics


class DirectorListAPIView(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class MovieListAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieReviewListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesReviewsSerializer

class ReviewListAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer




















# @api_view(['GET', 'POST'])
# def director_view(request):
#     if request.method == 'GET':
#         directors = Director.objects.all()
#         data = DirectorSerializer(directors, many=True).data
#         return Response(data=data)
#     else:
#         serializer = DirectorValidSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
#                             data={'error': serializer.errors})
#         name = request.data.get('name', '')
#         # print(name)
#         director = Director.objects.create(name=name)
#         return Response()
#
#
# @api_view(['GET', 'DELETE', 'PUT'])
# def director_detail_view(request, id):
#     try:
#         director = Director.objects.get(id=id)
#     except Director.DoesNotExist:
#         return Response(data={'fatal': 'Director not found :('}, status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = DirectorSerializer(director)
#         return Response(data=serializer.data)
#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT,
#                         data={'message': "director deleted successfully"})
#     elif request.method == 'PUT':
#         name = request.data.get('name')
#         director = Director()
#         director.name = name
#         director.save()
#         return Response(data={'message': 'director name was changed',
#                               'director': DirectorSerializer(director).data})
#
#
# @api_view(['GET', 'POST'])
# def movie_view(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(data=serializer.data)
#     else:
#         title = request.data.get('title', '')
#         description = request.data.get('description', '')
#         duration = request.data.get('duration', '')
#         director_id = request.data.get('director_id', 0)
#         movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
#         return Response()
#
#
# @api_view(['GET', 'DELETE', 'PUT'])
# def movie_detail_view(request, id):
#     try:
#         movie = Movie.objects.get(id=id)
#     except Movie.DoesNotExist:
#         return Response(data={'fatal': 'Movie not found :('}, status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = MovieSerializer(movie)
#         return Response(data=serializer.data)
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         title = request.data.get('title')
#         description = request.data.get('description', '')
#         duration = request.data.get('duration', 'more than hour')
#         director_id = request.data.get('director_id', 'google it')
#         movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
#         return Response(data={'message': 'movie was successfully changed',
#                               'movie': MovieSerializer(movie).data})
#
#
# @api_view(['GET'])
# def movies_reviews_view(request):
#     movies = Movie.objects.all()
#     serializer = MoviesReviewsSerializer(movies, many=True)
#     return Response(data=serializer.data)
#
#
# @api_view(['GET', 'POST'])
# def review_view(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(data=serializer.data)
#     else:
#         author_id = request.data.get('author_id', 0)
#         text = request.data.get('text', '')
#         movie_id = request.data.get('movie_id', 0)
#         stars = request.data.get('stars', 5)
#         review = Review.objects.create(author_id=author_id, text=text, movie_id=movie_id, stars=stars)
#         return Response()
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail_view(request, id):
#     try:
#         review = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(data={'fatal': 'review not found :( '}, status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = ReviewSerializer(review)
#         return Response(data=serializer.data)
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         author_id = request.data.get('author_id', 0)
#         text = request.data.get('text', 'nice one')
#         movie_id = request.data.get('movie_id', 0)
#         stars = request.data.get('stars', 5)
#         review = Review.objects.create(author_id=author_id, text=text, movie_id=movie_id, stars=stars)
#         return Response(data={'message': 'review was created and changed',
#                               'review': ReviewSerializer(review).data})










#