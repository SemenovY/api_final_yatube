"""Навигация и роутеры."""
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

app_name = 'api'


router_v1 = DefaultRouter()

router_v1.register('posts', PostViewSet, basename='post-list')
router_v1.register('groups', GroupViewSet, basename='group-list')
router_v1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='comment-list'
                   )

router_v1.register('follow', FollowViewSet, basename='follow-list')
# router_v1.register(
#     r'profile/<str:username>/follow/',
#     FollowViewSet,
#     basename='profile_follow-list',
# )
# router_v1.register(
#     r'profile/<str:username>/unfollow/',
#     FollowViewSet,
#     basename='profile_unfollow-list',
# )

urlpatterns = [
    path('v1/', include(router_v1.urls), name='api-root'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
