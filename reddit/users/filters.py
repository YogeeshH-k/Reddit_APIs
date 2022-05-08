from rest_framework.filters import BaseFilterBackend


class UserPostFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        user_id = request.id
        return queryset.filter(post_user_id=user_id)

