from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers

class LogInSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class RegisterSerializer(LogInSerializer):
    password_confirm = serializers.CharField()
    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise serializers.ValidationError('This user already exists!')

    def validate(self, validated_data):
        password = validated_data.get('password')
        password_confirm = validated_data.get('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('passwords do not match')
        validated_data.pop('password_confirm')
        return validated_data





# class RegisterSerializer(serializers.ModelSerializer):
#     username = serializers.CharField()
#     email = serializers.EmailField()
#     password = serializers.CharField(min_length=6, read_only=True)
#     password_confirm = serializers.CharField(min_length=6, read_only=True)
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password', 'password_confirm')
#
#         def validate(self, validated_data):
#             password = validated_data.get('password')
#             password_confirm = validated_data.get('password_confirm')
#             if password != password_confirm:
#                 raise serializers.ValidationError('passwords do not match')
#             return validated_data
#         def create(self, validated_data):
#             """this function is called when self.save() method will work """
#             username = validated_data.get('username')
#             email = validated_data.get('email')
#             password = validated_data.get('password')
#             user = User.objects.create_user(username=username, email=email, password=password)
#             return user

# class LogInSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     email = serializers.EmailField()
#     password = serializers.CharField(
#         label='Password',
#         style={'input_type': 'password'},
#         # trim_whitespace=False
#     )
#     def validate(self, validated_data):
#         username = validated_data.get('username')
#         email = validated_data.get('email')
#         password = validated_data.get('password')
#         if username  and password:
#             user = authenticate(request=self.context.get('request'), username=username, email=email,
#                                 password=password)
#             if not user:
#                 message = 'Unable to log in with provided credentials'
#                 raise serializers.ValidationError(message, code='authorization')
#         else:
#             message = 'Must include "username", "email" and "password"'
#             raise serializers.ValidationError(message, code='authorization')
#
#         validated_data['user'] = user
#         return validated_data