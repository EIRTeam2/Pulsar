from django.contrib import admin
from .models import Project, ProjectUserData, User, Task, Milestone, Category, DesignElement, Platform
# Register your models here.
admin.site.register(Project, admin.ModelAdmin)
admin.site.register(ProjectUserData, admin.ModelAdmin)
admin.site.register(User, admin.ModelAdmin)
admin.site.register(Task, admin.ModelAdmin)
admin.site.register(Milestone, admin.ModelAdmin)
admin.site.register(Category, admin.ModelAdmin)
admin.site.register(DesignElement, admin.ModelAdmin)
admin.site.register(Platform, admin.ModelAdmin)
