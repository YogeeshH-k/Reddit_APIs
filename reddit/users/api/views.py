from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from reddit.users.models import User
from reddit.users.api.serializers import UserDetailsSerializer, UserListSerializer, EmailSignupSerializer

from reddit.users.tasks import send_forgot_username_mail


class EmailSignupView(generics.CreateAPIView):
    serializer_class = EmailSignupSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = RefreshToken.for_user(user)
            data = EmailSignupSerializer(instance=user).data
            response_data = {
                'access': str(token.access_token),
                'refresh': str(token)
            }
            print(response_data)

            return Response("success")
        else:
            return Response("Request Failed")


class UserDetailsUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        data = request.data
        serializer = self.get_serializer(user, data=data, partial=True)
        if not serializer.is_valid():
            return Response('Please enter valid Data')
        serializer.save()
        updated_data = UserDetailsSerializer(instance=user).data
        return Response(f'Successfully updated data :{updated_data}')


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


class RequestForgotUsernameMailView(generics.CreateAPIView):
    serializer_class = UserDetailsSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        user = User.objects.get(email=email)
        send_forgot_username_mail(user.username, email)
        return Response("Success")


# class LogoutView(generics.CreateAPIView):
#     permission_classes = (IsAuthenticated,)
#
#     def create(self, request, *args, **kwargs):
#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response("Successfully Logged out")
#
#         except Exception as e:
#             print(e)
#             return Response("Bad request, please try again")
