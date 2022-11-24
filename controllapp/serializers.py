from rest_framework import serializers
from .models import *


# All device serializers

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields="__all__"
        depth = 1




class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"
        depth = 1



class DeviceSerializers(serializers.ModelSerializer):
    class Meta:
        model=Device
        fields="__all__"
        depth = 1
        
# main serializers its help to track all data
class AssetsTrackserializers(serializers.ModelSerializer):
    class Meta:
        model=Assets_management
        fields="__all__"
        depth = 2
        
        
