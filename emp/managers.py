from django.db import models
import datetime

class EmployeeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter()


    def all_employees(self):  
        return super().get_queryset()


    def all_blocked_employees(self):  
       return super().get_queryset().filter(is_blocked=True)





    


