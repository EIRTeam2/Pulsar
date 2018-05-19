# api/resources.py

from tastypie.resources import ModelResource
from .models import Task, Project, DesignElement
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import SessionAuthentication
from tastypie import fields
from tastypie.exceptions import BadRequest
from tastypie.serializers import Serializer
import json
class VerboseSerializer(Serializer):
    """
    Gives message when loading JSON fails.
    """
    # Tastypie>=0.9.6,<=0.11.0
    def from_json(self, content):
        """
        Override method of `Serializer.from_json`. Adds exception message when loading JSON fails.
        """
        print(content)
        try:
            return json.loads(content)
        except ValueError as e:

            raise BadRequest(u"Incorrect JSON format: Reason: \"{}\" (See www.json.org for more info.)".format(e.message))

class TaskResource(ModelResource):
    class Meta:
        queryset = Task.objects.all()
        resource_name = 'task'
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()
        serializer = VerboseSerializer(formats=['json'])

class DesignElementResource(ModelResource):
    parent = fields.ForeignKey('self', 'parent', null=True, full=False)
    children = fields.ToManyField('self', 'children', full=True, null=True)
    class Meta:
        queryset = DesignElement.objects.all()
        resource_name = 'design_element'
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()
        serializer = VerboseSerializer(formats=['json'])

class ProjectResource(ModelResource):
    tasks = fields.ToManyField(TaskResource, 'tasks', full=True)
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'project'
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()
