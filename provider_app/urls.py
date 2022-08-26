from django.urls import path
from . import views

#create routes for Provider portal
urlpatterns=[
    path('provider/', views.Home_Provider.as_view(), name='provider'),
    path('provider/schedule', views.Schedule.as_view(), name='schedule'),
    path('provider/client_list', views.Client_list.as_views(), name='client_list')

]
