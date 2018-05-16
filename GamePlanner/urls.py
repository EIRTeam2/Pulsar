from django.urls import path

from . import views

urlpatterns = [
    path('test', views.test, name='test'),
    path('projects/', views.ProjectListView.as_view(), name='project_list'),
    path('project/create', views.create_project, name='create_project'),
    path('project/<slug:slug>/', views.ProjectView.as_view(), name="project_summary"),
    path('project/<slug:slug>/create_task/', views.create_task, name="create_task")
]
