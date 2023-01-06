"""Админка."""
from django.conf import settings
from django.contrib import admin

from .models import Comment, Follow, Group, Post


class PostAdmin(admin.ModelAdmin):
    """Админка для модели Post."""
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = settings.EMPTY_VALUE


class GroupAdmin(admin.ModelAdmin):
    """Админка для модели Group."""
    list_display = (
        'pk',
        'title',
        'slug',
        'description',
    )
    list_editable = ('title',)
    search_fields = ('description',)
    empty_value_display = settings.EMPTY_VALUE


class CommentAdmin(admin.ModelAdmin):
    """Админка для модели Comment."""
    list_display = (
        'pk',
        'post',
        'text',
        'author',
    )
    list_editable = ('text',)
    search_fields = ('author',)
    empty_value_display = settings.EMPTY_VALUE


class FollowAdmin(admin.ModelAdmin):
    """Админка для модели Follow."""
    list_display = (
        'pk',
        'user',
        'following',
    )
    list_editable = ('user',)
    search_fields = ('following',)
    empty_value_display = settings.EMPTY_VALUE


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
