from django.db import models
from emp.utility import code_format
from emp.managers import EmployeeManager
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ('department')
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    department = models.ForeignKey(Department,verbose_name =_('department'),on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    contactnum = models.IntegerField()
    email = models.EmailField(max_length=30, null=True)
    employeeid = models.CharField(_('Employee Id Number'),max_length=5,null=True,blank=True)
    
    objects = EmployeeManager()
    class Meta:
        verbose_name = ('Employee')

    def __str__(self):
        return self.get_full_name

    @property
    def get_full_name(self):
        fullname = ''
        firstname = self.firstname
        lastname = self.lastname
        if (firstname and lastname):
            fullname = firstname + ' ' + lastname
        return fullname

    def save(self, *args, **kwargs):

        get_id = self.employeeid
        data = code_format(get_id)
        self.employeeid = data
        super().save(*args, **kwargs)
        # print(self.employeeid)
        
    @property
    def can_apply_leave(self):
        pass
