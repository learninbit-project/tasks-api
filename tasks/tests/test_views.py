from unittest.mock import patch

from django.test import TestCase
from rest_framework.test import APIClient

from users.tests.factories import AdminUserFactory, UserFactory

from ..serializers import TaskCategorySerializer, TaskSerializer
from .factories import TaskCategoryFactory, TaskFactory


class TestTask(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.instance = TaskFactory(created_by=self.user)

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list Task instances"""

        resp = self.client.get("/api/v1/tasks/task/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that Task collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/tasks/task/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_list_search(self):
        """Test that Task collection can be searched by"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(
            "/api/v1/tasks/task/",
            {
                "label__icontains": self.instance.label,
            },
        )
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve Task instances"""

        resp = self.client.get(f"/api/v1/tasks/task/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of Task can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/tasks/task/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new Task"""

        resp = self.client.post("/api/v1/tasks/task/")
        self.assertEqual(resp.status_code, 403)

    @patch("tasks.views.TaskViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for Task"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = TaskSerializer(self.instance).data

        resp = self.client.post("/api/v1/tasks/task/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with(created_by=self.user)

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing Task"""

        resp = self.client.patch(f"/api/v1/tasks/task/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test Task update"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.patch(f"/api/v1/tasks/task/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete Task"""

        resp = self.client.delete(f"/api/v1/tasks/task/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test Task deletion"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.delete(f"/api/v1/tasks/task/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)


class TestTaskCategory(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.instance = TaskCategoryFactory(created_by=self.user)

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list TaskCategory instances"""

        resp = self.client.get("/api/v1/tasks/task-category/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that TaskCategory collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/tasks/task-category/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_list_search(self):
        """Test that TaskCategory collection can be searched by"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(
            "/api/v1/tasks/task-category/",
            {
                "label__icontains": self.instance.label,
            },
        )
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve TaskCategory instances"""

        resp = self.client.get(f"/api/v1/tasks/task-category/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of TaskCategory can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/tasks/task-category/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new TaskCategory"""

        resp = self.client.post("/api/v1/tasks/task-category/")
        self.assertEqual(resp.status_code, 403)

    @patch("tasks.views.TaskCategoryViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for TaskCategory"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = TaskCategorySerializer(self.instance).data

        resp = self.client.post("/api/v1/tasks/task-category/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with(created_by=self.user)

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing TaskCategory"""

        resp = self.client.patch(f"/api/v1/tasks/task-category/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test TaskCategory update"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.patch(f"/api/v1/tasks/task-category/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete TaskCategory"""

        resp = self.client.delete(f"/api/v1/tasks/task-category/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test TaskCategory deletion"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.delete(f"/api/v1/tasks/task-category/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)
