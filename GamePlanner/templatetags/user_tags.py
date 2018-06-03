from django import template
from GamePlanner.forms import TaskForm
import json
register = template.Library()

@register.filter(name = 'format_username')
def format_username(value):
    result = "{} {} (@{})".format(value.first_name, value.last_name ,value.username)
    return result

@register.filter(name = 'format_cost')
def format_cost(value, project):
    return project.format_cost(value)

@register.filter(name = 'get_task_form')
def get_task_form(value):
    return TaskForm(project=value)

@register.filter(name = 'serialize')
def get_task_form(value):
    return json.dumps(value.serializable_object())
