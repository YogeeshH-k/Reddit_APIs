from django.urls import path
from .views import UserListView, UserDetailView, UserPostsView

urlpatterns = [
    path('posts/list', UserPostsView.as_view(), name='user posts'),
    path('list', UserListView.as_view(), name='user list'),
    path('<str:id>', UserDetailView.as_view(), name='user detail'),
]
