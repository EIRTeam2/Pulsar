# posts/views.py
from rest_framework import generics

from .models import Project, User, Task, Milestone, DesignElement
from .serializers import ProjectSerializer, UserSerializer, TaskSerializer, MilestoneSerializer, DesignElementSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework import views
from rest_framework import permissions
from .permissions import IsInProject
from django.db.models import Q

def filter_user_projects(user, projects):
    query_filter = Q(project_users_data__user=user) | Q(owner=user) 
    return projects.filter(query_filter)

class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsInProject,)
    def get_queryset(self):
        return filter_user_projects(self.request.user, self.get_queryset())
class ProjectDetail(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsInProject,)

    def get_queryset(self):
        return filter_user_projects(self.request.user, self.get_queryset())

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_fields = ('slug',)

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        return filter_user_projects(self.request.user, queryset)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get_object(self):
        pk = self.kwargs.get('pk')

        if pk == "current":
            return self.request.user

        return super(UserViewSet, self).get_object()

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_fields = ('project', 'id', 'milestone',)

class MilestoneViewSet(viewsets.ModelViewSet):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer
    filter_fields = ('project',)

class DesignElementViewSet(viewsets.ModelViewSet):
    queryset = DesignElement.objects.all()
    serializer_class = DesignElementSerializer
    filter_fields = ('project',)