from django.urls import path
from reddit.users.api.views import UserListView, UserDetailView, EmailSignupView, UserDetailsUpdateView, \
    RequestForgotUsernameMailView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('signup/email', EmailSignupView.as_view(), name='email signup'),
    path('profile/edit', UserDetailsUpdateView.as_view(), name='edit profile'),
    path('list', UserListView.as_view(), name='user list'),
    path('<str:id>', UserDetailView.as_view(), name='user detail'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('forgot/username', RequestForgotUsernameMailView.as_view(), name='forgot username'),
    # path('reset_password', name='forgot password'),
    # path('logout', LogoutView.as_view(), name='logout'),
]
