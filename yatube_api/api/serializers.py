"""Сериализаторы для моделей пост."""
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Post, Group, Follow


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Post."""
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        # TODO: del
        # fields = '__all__'
        model = Post
        fields = ('id', 'text', 'group', 'author', 'image', 'pub_date')


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group."""

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment."""
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.SlugRelatedField(read_only=True, slug_field='pk')

    class Meta:
        # TODO: fields = '__all__'
        model = Comment
        fields = ('id', 'text', 'author', 'post', 'created')


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Follow."""
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='following'
    )
    user = serializers.SlugRelatedField(read_only=True, slug_field='follower')

    class Meta:
        # TODO: fields = '__all__'
        model = Follow
        fields = ('user', 'author')
