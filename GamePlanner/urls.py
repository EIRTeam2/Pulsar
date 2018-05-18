from django.urls import path

from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('test', views.test, name='test'),
    path('projects/', views.ProjectListView.as_view(), name='project_list'),
    path('project/create', views.create_project, name='create_project'),
    path('project/<slug:slug>/', views.ProjectView.as_view(), name="project_summary"),
    path('project/<slug:slug>/create_task/', login_required(views.CreateTaskView.as_view()), name="create_task"),
    path('project/<slug:slug>/kanban/', views.kanban, name="kanban")
]
