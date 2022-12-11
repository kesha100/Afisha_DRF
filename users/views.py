from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(**serializer.validated_data)
        return Response('Successfully signed up!')


class LogInAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password =request.data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={'message': 'User credentials are not correct' })
        token, created = Token.objects.get_or_create(user=user)
        # print(created)
        return Response(data={'key': token.key})

class LogOutAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    def post(self, request):
        user = request.user
        Token.objects.get(user=user).delete()
        return Response(data={'message': 'Successfully loged out'}, status=status.HTTP_200_OK)





# class LogInAPIView(ObtainAuthToken):
#     serializer_class = LogInSerializer
#
# class LogOutAPIView(APIView):
#     permission_classes = [IsAuthenticated, ]
#
#     def post(self, request):
#         user = request.user
#         Token.objects.filter(user=user).delete()
#         return Response('Successfully loged out!', status=status.HTTP_200_OK)

