from django.db.models import Sum
from django.db import models
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_spectacular.utils import extend_schema
from django_filters import rest_framework as filters

from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer


@extend_schema(tags=["Employee"])
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('unit_id', 'last_name')


@extend_schema(tags=["Departament"])
class DepartmentViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Department.objects.annotate(num_employees=models.Count('employee'), total_salary=Sum('employee__salary'))
    serializer_class = DepartmentSerializer
