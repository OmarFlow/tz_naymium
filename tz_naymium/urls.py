from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, EmployeeViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)


urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
    path('api/', include(router.urls)),
    path("admin/", admin.site.urls),
]
