from django.db.models.query import QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from . import permissions
from .models import Task, TaskCategory
from .serializers import TaskCategorySerializer, TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    lookup_field = "external_id"
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.TaskPermission,)
    filter_backend = [DjangoFilterBackend]
    filterset_fields = {
        "label": ["icontains"],
    }

    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(created_by__id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskCategoryViewSet(viewsets.ModelViewSet):
    lookup_field = "external_id"
    queryset = TaskCategory.objects.all()
    serializer_class = TaskCategorySerializer
    permission_classes = (permissions.TaskCategoryPermission,)
    filter_backend = [DjangoFilterBackend]
    filterset_fields = {
        "label": ["icontains"],
    }

    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(created_by__id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
