from django.db import models
from django.contrib.auth.models import AbstractUser
from .slugify import unique_slugify
from simplemde.fields import SimpleMDEField
from django.forms.models import model_to_dict
from django.core import serializers

import math
import datetime
class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)


class Project(models.Model):
    HOURS = "HOURS"
    DAYS = "DAYS"
    POINTS = "POINTS"
    COST_METRIC_CHOICES = (
        (HOURS, 'Hours'),
        (DAYS, 'Days'),
        (POINTS, 'Points'),
    )
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_projects", null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    creation_date = models.DateTimeField('Creation Time', auto_now_add=True)
    description = SimpleMDEField('Project Description')
    project_info = models.TextField('General Project Information')
    cost_metric = models.CharField(max_length=20, choices=COST_METRIC_CHOICES, default=HOURS)

    def serializable_object(self):
        dict = model_to_dict(self)
        dict["element_types"] = []
        dict["milestones"] = []
        for element_type in self.element_types.all():
            dict["element_types"].append(model_to_dict(element_type))
        for milestone in self.milestones.all():
            dict["milestones"].append(model_to_dict(milestone))

        return dict

    def save(self, *args, **kwargs):
        # Only save slugs on first save
        if not self.id:
            print(self.name)
            unique_slugify(self, self.name)
        super(Project, self).save(*args,**kwargs)

    def get_pending_tasks(self):
        return self.tasks.all().exclude(stage=Task.COMPLETED)

    def get_closed_tasks(self):
        return self.tasks.filter(stage=Task.COMPLETED)
    def get_estimated_cost(self):
        cost = 0
        for task in self.tasks.all():
            cost += task.estimated_cost
        return cost

    def get_final_cost(self):
        cost = 0
        for task in self.tasks.all():
            cost += task.final_cost
        return cost

    def get_remaining_cost(self):
        remaining_cost =  self.get_estimated_cost() - self.get_final_cost()
        if remaining_cost < 0:
            remaining_cost = 0
        return remaining_cost

    def format_cost(self, cost):
        if self.cost_metric == self.HOURS:
            final_string = "{} {}"
            minutes, hours = math.modf(cost)

            hours_string = ""
            minutes_string = ""

            if hours > 0:
                hours_string = "{}h".format(int(hours))
            if minutes > 0:
                minutes_string = "{}m".format(int(minutes*60))

            if minutes <= 0 and hours <= 0:
                final_string = "0h"

            return final_string.format(hours_string, minutes_string).strip()

    def get_project_completion(self):
        project_completion = 0.0
        for task in self.tasks.all():
            if task.stage == task.COMPLETED:
                project_completion += 1.0

        if self.tasks.all().count() > 0:
            project_completion = project_completion / self.tasks.all().count()
        return project_completion
    def __str__(self):
        return self.name
class Platform(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="platforms", null=True, blank=True)
    def __str__(self):
        return self.name

class Milestone(models.Model):
    name = models.CharField(max_length=200)
    description = SimpleMDEField('Project Description')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="milestones", null=True, blank=True)
    creation_date = models.DateTimeField('Creation Time', auto_now_add=True)
    starting_date = models.DateTimeField('Starting Date', blank=True, null=True)
    due_date = models.DateTimeField('Due Date', blank=True, null=True)
    closing_date = models.DateTimeField('Closing Date', blank=True, null=True)
    def __str__(self):
        return self.name
class ProjectUserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_users_data")
    is_admin = models.BooleanField("Is an administrator", default=False)
    is_active = models.BooleanField("Is the user active", default=False)
    join_date = models.DateTimeField('Joining date', auto_now_add=True)
    def __str__(self):
        return self.user.username
class Category(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="categories")
    creation_date = models.DateTimeField('Creation Time', auto_now_add=True)
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    parent_category = models.ForeignKey(Category, related_name="sub_categories", on_delete=models.CASCADE)
    creation_date = models.DateTimeField('Creation Time', auto_now_add=True)
    def __str__(self):
        return self.name

class ElementType(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="element_types")
    creation_date = models.DateTimeField('Creation Time', auto_now_add=True)

    def __str__(self):
        return self.name

class DesignElement(models.Model):
    name = models.CharField(max_length=300)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name="children")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True, related_name="design_elements")
    element_type = models.ForeignKey(ElementType, on_delete=models.CASCADE, related_name="elements")
    description = SimpleMDEField("Element description", null=True, blank=True)
    def serializable_object(self):
        obj = {'name': self.name, 'children': [], 'description': self.description, 'tasks': [], 'id': self.pk, 'element_type': model_to_dict(self.element_type)}
        for child in self.children.all():
            obj['children'].append(child.serializable_object())
        for task in self.tasks.all():
            obj["tasks"].append(task.serializable_object())
        return obj
    def __str__(self):
        return self.name



class Task(models.Model):

    PLANNED = "PLANNED"
    IN_PROGRESS = "IN_PROGRESS"
    TESTING = "TESTING"
    COMPLETED = "COMPLETED"
    STAGE_CHOICES = (
        (PLANNED, 'Planned'),
        (IN_PROGRESS, 'In Progress'),
        (TESTING, 'Testing'),
        (COMPLETED, 'Completed'),
    )

    title = models.CharField(max_length=300)
    description = SimpleMDEField('Task Description')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks", blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="tasks", on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, related_name="tasks", on_delete=models.CASCADE)
    design_element = models.ForeignKey(DesignElement, on_delete=models.CASCADE, related_name="tasks")
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    estimated_cost = models.FloatField("Estimated time cost")
    final_cost = models.FloatField("Final cost", default=0.0)
    starting_date = models.DateTimeField('Starting Date', null=True, blank=True)
    due_date = models.DateTimeField('Due Date', null=True, blank=True)
    creation_date = models.DateTimeField('Creation date', auto_now_add=True)
    completion_date = models.DateTimeField('Completion date', null=True, blank=True)
    update_date = models.DateTimeField('Last update date', null=True, blank=True)
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assigned_tasks")
    stage = models.CharField(max_length=200, choices=STAGE_CHOICES, default="PLANNED")

    def serializable_object(self):
        obj = {'title': self.title, 'category': model_to_dict(self.category), 'description': self.description,
                'estimated_cost': self.estimated_cost, 'final_cost': self.final_cost, 'stage': self.stage, 'id': self.pk,
                'design_element': model_to_dict(self.design_element), 'sub_category': model_to_dict(self.sub_category),
                'milestone': model_to_dict(self.milestone)}

        return obj

    def __str__(self):
        return self.title
