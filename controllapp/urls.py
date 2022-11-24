from django.urls import path,include
from .import views 
from .urls import *
from .views import *

# all in one 
from rest_framework import routers
route=routers.DefaultRouter()
route.register("",allassets,basename="allassets")
route.register("employee",EmployeeView,basename="employee")
route.register("device",DeviceExtraview,basename="device")

# # end allin one
urlpatterns = [
    
    path('',include(route.urls)),
    path('company/',CompanyView.as_view(),name="company"),
    path('company/<int:id>/',CompanyView.as_view(),name="company"),
    path('DeviceAddView',DeviceView.as_view(),name='DeviceAddView'),
    
]
