from django.urls import path

from .views import *
urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LogInAPIView.as_view()),
    path('logout/', LogOutAPIView.as_view()),
]