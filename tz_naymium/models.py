from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    director = models.OneToOneField('Employee', on_delete=models.SET_NULL, null=True, blank=True, related_name='department')

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, db_index=True)
    photo = models.ImageField(upload_to='employees/', null=True, blank=True)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    age = models.IntegerField()
    unit = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='employee')

    def __str__(self):
        return self.name