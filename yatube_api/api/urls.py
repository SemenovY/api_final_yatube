"""Навигация и роутеры."""
from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

app_name = 'api'


router_v1 = SimpleRouter()

router_v1.register('posts', PostViewSet, basename='post-list')
router_v1.register('groups', GroupViewSet, basename='group-list')
router_v1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='comment-list',
                   )
# TODO: Переписать токен
urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router_v1.urls), name='api-root'),
]
