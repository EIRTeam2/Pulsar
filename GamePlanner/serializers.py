from rest_framework import serializers
from .models import Project, User, ProjectUserData, Task, Milestone, DesignElement




class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'username',)
        model = User

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'status', 'title', 'category', 'milestone', 'sub_category', 'project', 'design_element',)
        model = Task

class ProjectUsersDataSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'is_admin', 'is_active', 'join_date',)
        model = ProjectUserData

class DesignElementSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'parent', 'project', 'element_type', 'description',)
        model = DesignElement

class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'description', 'project', 'creation_date', 'starting_date', 'due_date', 'closing_date',)
        model = Milestone

class ProjectSerializer(serializers.ModelSerializer):
    pending_tasks = serializers.ReadOnlyField(source='pending_tasks.count')

    closed_tasks = serializers.ReadOnlyField(source='closed_tasks.count')
    total_tasks = serializers.ReadOnlyField(source='tasks.count')
    project_completion = serializers.ReadOnlyField()
    estimated_cost = serializers.ReadOnlyField()
    final_cost = serializers.ReadOnlyField()
    remaining_cost = serializers.ReadOnlyField()

    project_users_data = ProjectUsersDataSerializer(many=True, read_only=True)
    owner = UserSerializer(read_only=True)
    class Meta:
        fields = ('id', 'name', 'slug', 'description', 'cost_metric', 'creation_date', 'owner', 'pending_tasks', 'closed_tasks', 'total_tasks', 'project_completion', 'estimated_cost', 'final_cost', 'remaining_cost', 
        'project_users_data', 'owner',)
        model = Project