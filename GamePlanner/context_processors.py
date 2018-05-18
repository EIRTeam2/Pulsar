from .forms import TaskForm
def global_forms(request):
    task_form = TaskForm
    return {'task_form': task_form}
