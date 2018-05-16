from django.contrib import admin
from .models import Project, ProjectUserData, User, Task
# Register your models here.
admin.site.register(Project, admin.ModelAdmin)
admin.site.register(ProjectUserData, admin.ModelAdmin)
admin.site.register(User, admin.ModelAdmin)
admin.site.register(Task, admin.ModelAdmin)
