from rest_framework import serializers

from models import Posts
from users.models import User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        exclude = ('id', 'created_on', 'updated_on', 'is_deleted')


class UserPostsSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)

    class Meta:
        model = User
        fields = ('username', 'profile_image', 'posts')
