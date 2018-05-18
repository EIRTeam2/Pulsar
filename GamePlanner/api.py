# api/resources.py

from tastypie.resources import ModelResource
from .models import Task, Project
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import SessionAuthentication
from tastypie import fields
class TaskResource(ModelResource):
    class Meta:
        queryset = Task.objects.all()
        resource_name = 'task'
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()

class ProjectResource(ModelResource):
    tasks = fields.ToManyField(TaskResource, 'tasks', full=True)
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'project'
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()
