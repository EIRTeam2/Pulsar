from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Project, ProjectUserData, Task, DesignElement
from .forms import CreateProjectForm, TaskForm
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
import json
# Create your views here.
def test(request):
    return render(request, 'test.html')



@login_required
def create_project(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            user = request.user
            project = Project(name=form.cleaned_data['name'],
                        description=form.cleaned_data['description'],
                        project_info=form.cleaned_data['project_info'],
                        cost_metric=form.cleaned_data['cost_metric'],
                        owner=request.user)
            project.save()
            user_data = ProjectUserData(user=user, project=project, is_admin=True, is_active=True)
            user_data.save()
            return HttpResponseRedirect(reverse('test') )
    else:
        form = CreateProjectForm()
    return render(request, 'views/new_project.html', {'form': form})



class CreateTaskView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = ["title", "description", "project", "milestone", "category", "stage",
    "platform", "estimated_cost", "final_cost", "due_date", "assigned_user", "design_element"]
    template_name="views/new_task.html"
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return HttpResponseRedirect(self.get_success_url())

@login_required
def kanban(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if request.method == 'POST':
        pass
    else:
        tasks = project.tasks.all()
        tasks = serializers.serialize('json', tasks)
        return render(request, 'views/task_list.html', {'project': project, 'tasks': tasks})

class ProjectView(generic.DetailView):
    model = Project
    template_name = 'views/project_summary.html'
@login_required
def game_design(request, slug):
    project = get_object_or_404(Project, slug=slug)
    nodes = []
    for design_element in DesignElement.objects.filter(parent=None, project=project):
        nodes.append(design_element.serializable_object())

    return render(request, 'views/project_game_design.html', {'project': project, 'nodes':json.dumps(nodes)})

class ProjectListView(generic.ListView):
    template_name = 'views/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.all()
