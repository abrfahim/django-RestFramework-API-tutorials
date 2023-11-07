from django.urls import path
from theapi import views


urlpatterns = [
    path('netcreate/', views.netschool_create, name='netcreate'),
    path('netcreate/<int:pk>/', views.netschool_create, name='netcreate'),
    path('network/<int:pk>/', views.NetSchoolCreate.as_view(), name='netschoolcreate'),
    path('netlist/', views.NetList.as_view(), name='netlist'),
    path('objcreate/', views.NetCreation.as_view(), name='objcreate'),
    path('objinfo/<int:pk>/', views.NetGet.as_view(), name='objinfo'),
    path('objupdate/<int:pk>/', views.NetUpdate.as_view(), name='objupdate'),
    path('objdelete/<int:pk>/', views.NetDestroy.as_view(), name='objdelete'),
]
