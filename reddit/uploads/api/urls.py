from django.urls import path

from reddit.uploads.api.views import UserPostsView, PostCreateView

urlpatterns = [
    path('user/posts', UserPostsView.as_view(), name='user posts'),
    path('post/create', PostCreateView.as_view(), name='create post'),
    ]


