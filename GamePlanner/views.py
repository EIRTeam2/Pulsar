from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Project, ProjectUserData
from .forms import CreateProjectForm, TaskForm
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

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
@login_required
def create_task(request, slug):
    project = get_object_or_404(Project, slug=slug)
    form = TaskForm(project=project)
    if request.method == 'POST':
        pass
    else:
        return render(request, 'views/new_task.html', {'project': project, 'form': form})

class ProjectView(generic.DetailView):
    model = Project
    template_name = 'views/project_summary.html'

class ProjectListView(generic.ListView):
    template_name = 'views/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.all()
