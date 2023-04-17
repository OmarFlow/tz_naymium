from django.contrib import admin
from .models import Employee, Department


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    ...


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        departament_id = request.resolver_match.kwargs.get('object_id')
        if db_field.name == "director":
            if departament_id:
                kwargs["queryset"] = Employee.objects.filter(unit_id=departament_id)
            else:
                kwargs["queryset"] = Employee.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
