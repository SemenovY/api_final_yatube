"""Сериализаторы для моделей Comment, Post, Group, Follow."""
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Post."""
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        """Поля для сериализатора укажем явно."""
        model = Post
        fields = ('id', 'author', 'text', 'pub_date', 'image', 'group')


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group."""

    class Meta:
        """Поля для Group укажем явно."""
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment."""
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.SlugRelatedField(read_only=True, slug_field='pk')

    class Meta:
        """Поля для Comment укажем явно."""
        model = Comment
        fields = ('id', 'author', 'text', 'created', 'post')


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Follow."""
    user = SlugRelatedField(read_only=True, slug_field='username',
                            default=serializers.CurrentUserDefault())

    following = SlugRelatedField(
        slug_field='username', queryset=User.objects.all(),
    )

    def validate(self, data):
        """Проверка подписки на себя."""
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!')
        return data

    class Meta:
        """Проверим на уникальность подписки на автора."""
        fields = ('user', 'following')
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]
