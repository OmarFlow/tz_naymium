from rest_framework import serializers

from .models import Employee, Department


class DepartmentSerializer(serializers.ModelSerializer):
    num_employees = serializers.IntegerField()
    total_salary = serializers.IntegerField()

    class Meta:
        model = Department
        fields = ['id', 'name', 'director', 'num_employees', 'total_salary']


class EmployeeSerializer(serializers.ModelSerializer):
    unit_name = serializers.CharField(source='unit.name', read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'last_name', 'photo', 'position', 'salary', 'age', 'unit', 'unit_name']