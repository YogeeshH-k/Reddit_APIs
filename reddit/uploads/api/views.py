from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.models import User
from serializers import PostSerializer, UserPostsSerializer


class UserPostsView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserPostsSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response = Response(serializer.data)
        return response


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Sucessfully posted")
        return Response("Invalid Request")
