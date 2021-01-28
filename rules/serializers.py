from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import UserColor
from django.contrib.auth.password_validation import validate_password


class UserColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserColor
        fields = ('color', 'user', )

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # validated_data.pop('color')
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        token = Token.objects.create(user=user)
        return user

class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'