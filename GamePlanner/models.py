from django.db import models

class Platform(models.Models):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Project(models.Models):
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField('Creation Time', auto_now_add=True)
    description = models.TextField('Project Description')
    project_info = models.TextField('General Project Information')

class Milestone(models.Models):
    name = models.CharField(max_length=200)
    description = models.TextField('Project Description')
    creation_date = models.DateTimeField('Creation Time', auto_now_add=True)
    starting_date = models.DateTimeField('Starting Date')
    due_date = models.DateTimeField('Due Date')
    closing_date = models.DateTimeField('Closing Date')

class ProjectUserData(models.Model):
    user = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    is_admin = models.BooleanField("Is an administrator")
    is_active model.BooleanField("Is the user active")
    join_date = models.DateTimeField('Joining date', auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    creation_date = models.DateTimeField('Creation Time', auto_now_add=True)

class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    creation_date = models.DateTimeField('Creation Time', auto_now_add=True)

class Task(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField('Project Description')
    creator = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    design_element = models.ForeignKey(DesignElement, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    estimated_cost = models.IntegerKey("Estimated time cost")
    final_cost = models.IntegerKey("Final cost")
    due_date = models.DateTimeField('Due Date')
    creation_date = models.DateTimeField('Creation date', auto_now_add=True)
    update_date = models.DateTimeField('Last update date')
    users = models.ManyToManyField(User)
    def save():
        super(models.Model,self).save()
