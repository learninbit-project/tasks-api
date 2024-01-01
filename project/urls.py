from django.urls import include, path, re_path
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from tasks.urls import tasks_router

from users.urls import users_router

schema_view = get_schema_view(
    openapi.Info(
        title="Tasks API",
        default_version="v1",
        description="API Server for Tasks",
        contact=openapi.Contact(email="mail@rithviknishad.dev"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.registry.extend(tasks_router.registry)
# router.registry.extend(users_router.registry)

urlpatterns = [
    path("api/docs/auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/v1/", include("openapi.urls")),
    path("api/v1/", include(router.urls)),
    # Auth
    # path("api/v1/auth/", include("dj_rest_auth.urls")),
    path(
        "api/v1/auth/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/v1/auth/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    # Swagger, Redoc and OpenAPI
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
