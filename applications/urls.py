from django.urls import path
from . import views

urlpatterns = [

    # path("", views.landing_page, name="landing"),
    path('job_list/',views.job_list, name ="job_list"),
    path('add/', views.job_create, name='job_create'),
    path("jobs/<int:pk>/edit/",views.edit_job,name="edit_job"),
    path("jobs/<int:pk>/delete/", views.delete_job, name="delete_job"), 
    path("jobs/<int:pk>/", views.job_detail, name="job_detail"),
   
    path("dashboard/", views.dashboard, name="dashboard"),

]
