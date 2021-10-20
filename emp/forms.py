from django import forms
from emp.models import Employee
from django.contrib.auth.models import User


class EmployeeCreateForm(forms.ModelForm):
    employeeid = forms.CharField()

    class Meta:
        model = Employee
        exclude = ['created', 'is_blocked', 'is_deleted', 'updated']
