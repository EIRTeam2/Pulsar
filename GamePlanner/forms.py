from django import forms
from .models import Project

class CreateProjectForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    cost_metric = forms.ChoiceField(choices=Project.COST_METRIC_CHOICES)
    project_info = forms.CharField()
