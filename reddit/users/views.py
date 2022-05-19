from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .filters import UserPostFilterBackend
from .models import User
from .serializers import UserDetailsSerializer, UserPostsSerializer, UserListSerializer, PostSerializer, \
    EmailSignupSerializer
from uploads.models import Posts


class EmailSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = EmailSignupSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = RefreshToken.for_user(user)
            data = EmailSignupSerializer(instance=user).data
            data['access'] = str(token.access_token)
            data['refresh'] = str(token)
            return Response("success", data=data)
        else:
            return Response("Request Failed")


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
    lookup_field = 'username'
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


