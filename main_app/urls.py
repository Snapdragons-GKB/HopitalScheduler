from django.urls import path
from . import views

#create routes for patient portal, maps to views.py
urlpatterns=[
    path('', views.Home, name='home'), 
    path('accounts/profile/', views.Home, name='home'), 
    path('patient/request/',views.Patient_Request, name='patient_request'), 
    path('patient/detail/', views.Patient_Details, name='patient_detail'), # needs to be added to path once db seeded
    path('patient/signup/', views.Signup.as_view(), name="signup"),
    path('patient/about/', views.About, name="about"),
   

#create routes for Scheduler/Admin portal
    # path('admin/', views.Home_Admin, name='admin'),
    # path('admin/patient_request/', views.Admin_Patient_Request.as_view(), name='admin_patient_request'),
    # path('admin/patient_list/', views.Admin_Patient_list.as_view(), name='admin_patient_list'),


    
]


