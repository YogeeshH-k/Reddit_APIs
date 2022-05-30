from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from uploads.models import Posts
from .models import User


class EmailSignupSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('email', 'password', 'username')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        exclude = ('id', 'created_on', 'updated_on', 'is_deleted')


class UserPostsSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)

    class Meta:
        model = User
        fields = ('username', 'profile_image', 'posts')


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'profile_image')


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'profile_image')
