from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('workstations/', views.workstation_list, name='workstation_list'),
    path('workstations/<int:workstation_id>/',
         views.workstation_detail, name='workstation_detail'),
    path('workstations/create/', views.workstation_create,
         name='workstation_create'),
    path('workstations/<int:workstation_id>/update/',
         views.workstation_update, name='workstation_update'),
    path('workstations/<int:workstation_id>/delete/',
         views.workstation_delete, name='workstation_delete'),

    path('schedules/', views.schedule_list, name='schedule_list'),
    path('schedules/<int:schedule_id>/',
         views.schedule_detail, name='schedule_detail'),
    path('schedules/create/', views.schedule_create, name='schedule_create'),
    path('schedules/<int:schedule_id>/update/',
         views.schedule_update, name='schedule_update'),
    path('schedules/<int:schedule_id>/delete/',
         views.schedule_delete, name='schedule_delete'),
]
