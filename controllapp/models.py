from django.db import models
from django.utils.html import mark_safe
import datetime
# Create your models here.


    


class Device(models.Model):
    device_name=models.CharField(max_length=200,blank=False,null=False)
    model_number=models.CharField(max_length=200,blank=False,null=False)
    image=models.ImageField(upload_to="all_assets",blank=False,null=False)
    device_serial_number=models.CharField(max_length=400,blank=False,null=False,unique=True)
    short_descriptions=models.TextField(blank=True,null=True)
    
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.device_name
    def image_tag(self):
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))


class Company(models.Model):
    company_name=models.CharField(max_length=200,blank=False,null=False)
    address=models.TextField(null=False,blank=False)
    def __str__(self):
        return self.company_name
class Employee(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    employee_name=models.CharField(max_length=400,blank=False,null=False)
    employee_image=models.ImageField(upload_to="employee",blank=False,null=False)
    employee_designation=models.CharField(max_length=100,blank=False,null=False)
    employee_id=models.CharField(max_length=100,blank=False,null=False)
    address=models.TextField(null=False,blank=False)
    phone=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.employee_name
    def image_tag(self):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.employee_image.url))



class Assets_management(models.Model):
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    device=models.ForeignKey(Device, on_delete=models.CASCADE)
    device_issue_date=models.DateField(("Device issue date"), default=datetime.date.today)
    due_date=models.DateField(("Due Date"), default=datetime.date.today)
    return_device=models.BooleanField(default=False)
    def __str__(self):
        return f"Employee Id = {self.employee.employee_id}"
    def device_modelSerial(self):
        return f"  Model number = {self.device.model_number} & Serial_number= {self.device.device_serial_number}"