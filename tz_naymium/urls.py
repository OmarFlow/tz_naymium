from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, DepartmentViewSet, EmployeeViewSet
from rest_framework import permissions
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)

# authenticated_router = DefaultRouter()
# authenticated_router.register(r'employees', EmployeeViewSet)

# schema_view = get_schema_view(
#    openapi.Info(
#       title="Naymium API",
#       default_version='v1',
#       description="API for working with company structure",
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
    path('api/', include(router.urls)),
    path("admin/", admin.site.urls),
]
