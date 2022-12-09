from django.db import models
from django.contrib.auth.models import User


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def movie_count(self):
        list_of_movies = [director for director in self.movies.all()]
        return len(list_of_movies)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    director = models.ForeignKey(Director, on_delete=models.SET_DEFAULT, default='google it', related_name='movies')

    def __str__(self):
        return self.title

    def rating(self):
            lst = [review.stars for review in self.reviews.all()]
            return (sum(lst) / len(lst)) if len(lst) != 0 else "No reviews yet"


class Review(models.Model):
    class ChoisesReview(models.IntegerChoices):
        BEST = 5
        GOOD = 4
        NOT_BAD = 3
        SOSO = 2
        CRINGE = 1
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(choices=ChoisesReview.choices, default=0)

    def __str__(self):
        return f'@{self.author.username} \nfor {self.movie.title} \n{self.text} ' if self.author is not None else '@Anonymous'
