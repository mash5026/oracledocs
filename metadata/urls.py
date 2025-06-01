from django.urls import path
from . import views


app_name='metadata'

urlpatterns = [
    path("", views.index, name="home"),
    path('tables/', views.table_metadata, name='tables'),
    path('views/', views.view_metadata, name='views'),
    path('programs/', views.procedure_metadata, name='programs'),
    path("jobs/", views.job_metadata, name="jobs"),
    path("jobs/logs/", views.job_logs, name="job_logs"),
    path("jobs/run-details/", views.job_run_details, name="job_run_details"),
]