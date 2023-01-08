"""Кастом миксин на создание и получение подписок."""
from rest_framework import mixins, viewsets


class CreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                        viewsets.GenericViewSet
                        ):
    """Кастом миксин, создаем объект и получаем список."""
    pass
