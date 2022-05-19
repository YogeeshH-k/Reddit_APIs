from django.urls import path
from .views import UserListView, UserDetailView, UserPostsView, EmailSignupView, UserDetailsUpdateView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('signup/email', EmailSignupView.as_view(), name='email signup'),
    path('profile/edit', UserDetailsUpdateView.as_view(), name='edit profile'),
    path('posts/list', UserPostsView.as_view(), name='user posts'),
    path('list', UserListView.as_view(), name='user list'),
    path('<str:id>', UserDetailView.as_view(), name='user detail'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
