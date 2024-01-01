from datetime import timezone

import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

from ..models import Task, TaskCategory

User = get_user_model()


class TaskCategoryFactory(DjangoModelFactory):
    class Meta:
        model = TaskCategory

    label = factory.Faker("bs")
    created_by = factory.SubFactory("users.tests.factories.UserFactory")
    meta = factory.Faker("json")


class TaskFactory(DjangoModelFactory):
    class Meta:
        model = Task

    label = factory.Faker("bs")
    created_by = factory.SubFactory("users.tests.factories.UserFactory")
    description = factory.Faker("bs")
