from django.contrib import admin
from .models import *
# Register your models here.
class deviceAdmin(admin.ModelAdmin):
    list_display=["__str__","model_number",'image_tag']
    list_per_page = 10
    search_fields =['device_name',]

admin.site.register(Device,deviceAdmin)

 
admin.site.register(Company)


class employeeAdmin(admin.ModelAdmin):
    list_display=["__str__","employee_id","image_tag"]
    list_per_page = 10
    search_fields =['employee_id',]

admin.site.register(Employee,employeeAdmin) 


class assetsManagementAdmin(admin.ModelAdmin):
    list_display=["__str__","employee","device","device_issue_date","device_modelSerial","return_device"]
    list_per_page = 10
    search_fields =['employee',]

admin.site.register(Assets_management,assetsManagementAdmin) 
    