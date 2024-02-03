from rest_framework import serializers

from .models import Task, TaskCategory
from utils.fields import ExternalIdRelatedField


class TaskCategorySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", read_only=True)

    class Meta:
        model = TaskCategory
        fields = ["id", "label", "description", "meta"]


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", read_only=True)
    category = ExternalIdRelatedField(
        queryset=TaskCategory.objects.all(), write_only=True, required=True
    )
    category_object = TaskCategorySerializer(source="category", read_only=True)

    class Meta:
        model = Task
        fields = ["id", "label", "category", "category_object", "meta", "description"]
