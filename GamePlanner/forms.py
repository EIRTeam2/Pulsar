from django import forms
from .models import Project, Task

class CreateProjectForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    cost_metric = forms.ChoiceField(choices=Project.COST_METRIC_CHOICES)
    project_info = forms.CharField()

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "project", "milestone", "category", "status",
        "platform", "estimated_cost", "final_cost", "due_date", "assigned_user", "design_element"]
    def __init__(self, *args, **kwargs):
        project = kwargs.pop('project')
        kwargs.update(initial={
            'project': project
        })
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['milestone'] = forms.ModelChoiceField(queryset = project.milestones.all())
        self.fields['assigned_user'] = forms.ModelChoiceField(queryset = project.project_users_data.all())
        self.fields['platform'] = forms.ModelChoiceField(queryset = project.platforms.all())
        self.fields['category'] = forms.ModelChoiceField(queryset = project.categories.all())
        self.fields['due_date'] = forms.DateTimeField()
