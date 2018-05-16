from django import template

register = template.Library()

@register.filter(name = 'format_username')
def format_username(value):
    result = "{} {} (@{})".format(value.first_name, value.last_name ,value.username)
    return result

@register.filter(name = 'format_cost')
def format_cost(value, project):
    return project.format_cost(value)
