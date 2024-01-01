from rest_framework import routers

from .views import TaskCategoryViewSet, TaskViewSet

tasks_router = routers.SimpleRouter()
tasks_router.register(r"tasks/task", TaskViewSet)
tasks_router.register(r"tasks/categories", TaskCategoryViewSet)
