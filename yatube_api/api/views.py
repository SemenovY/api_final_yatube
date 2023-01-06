"""Viewset для работы с моделями."""
from django.shortcuts import get_object_or_404

from rest_framework import filters, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from .permissions import AuthorOrReadOnly
from posts.models import Group, Post, Follow
from .serializers import CommentSerializer, GroupSerializer, \
    PostSerializer, FollowSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Post."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly, )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Получаем автора при создании."""
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        """При запросе на изменение данных
        осуществлять проверку прав."""
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, serializer):
        """При запросе на удаление данных
        осуществлять проверку прав."""
        if serializer.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        super().perform_destroy(serializer)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для модели Group."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AuthorOrReadOnly, )


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Comment."""
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly, )

    def get_queryset(self):
        """Получаем кверисет для модели Comment."""
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        new_queryset = post.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        """Получаем автора при создании."""
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)

    def perform_update(self, serializer):
        """При запросе на изменение данных
        осуществлять проверку прав."""
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, serializer):
        """При запросе на удаление данных
        осуществлять проверку прав."""
        if serializer.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        super().perform_destroy(serializer)


class FollowViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Follow."""
    permission_classes = (IsAuthenticated, )
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username', )

    def get_queryset(self):
        """Получаем кверисет для модели Follow."""
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        """Получаем автора при создании."""
        serializer.save(user=self.request.user)
