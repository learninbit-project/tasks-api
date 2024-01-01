from django.db import models
from utils.models import BaseModel


class TaskCategory(BaseModel):
    label = models.CharField(max_length=255)
    description = models.TextField(null=True)
    meta = models.JSONField(null=True)

    created_by = models.ForeignKey(
        "users.User", related_name="+", on_delete=models.PROTECT, editable=False
    )

    def __str__(self):
        return self.label


class Task(BaseModel):
    label = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    meta = models.JSONField(null=True)

    created_by = models.ForeignKey(
        "users.User", related_name="+", on_delete=models.PROTECT, editable=False
    )

    def __str__(self):
        return self.label
