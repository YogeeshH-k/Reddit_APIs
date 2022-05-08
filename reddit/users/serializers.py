from rest_framework import serializers

from uploads.models import Posts
from .models import User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        exclude = ('id', 'created_on', 'updated_on', 'is_deleted')


class UserPostsSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)

    class Meta:
        model = User
        fields = ('user_id', 'profile_image', 'posts')


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'user_id', 'first_name', 'last_name', 'profile_image')


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('id', 'posts', 'created_on', 'updated_on', 'is_deleted')
