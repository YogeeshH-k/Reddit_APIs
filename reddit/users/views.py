from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from rest_framework.response import Response

from .filters import UserPostFilterBackend
from .models import User
from .serializers import UserDetailsSerializer, UserPostsSerializer, UserListSerializer, PostSerializer
from uploads.models import Posts


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response = Response(serializer.data)
        return response


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer
    lookup_field = 'user_id'
    lookup_url_kwarg = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response = Response(serializer.data)
        return response


class UserPostsView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserPostsSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response = Response(serializer.data)
        return response


