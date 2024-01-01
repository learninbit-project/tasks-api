from rest_framework import serializers

from .models import Task, TaskCategory


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", read_only=True)

    class Meta:
        model = Task
        fields = ["id", "label", "meta", "description"]


class TaskCategorySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", read_only=True)

    class Meta:
        model = TaskCategory
        fields = ["id", "label", "description", "meta"]
