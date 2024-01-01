from django.test import TestCase

from ..models import Task, TaskCategory
from .factories import TaskCategoryFactory, TaskFactory


class TaskCategoryTestCase(TestCase):
    def test_create_task_category(self):
        """Test that TaskCategory can be created using its factory."""

        obj = TaskCategoryFactory()
        assert TaskCategory.objects.all().get() == obj


class TaskTestCase(TestCase):
    def test_create_task(self):
        """Test that Task can be created using its factory."""

        obj = TaskFactory()
        assert Task.objects.all().get() == obj
