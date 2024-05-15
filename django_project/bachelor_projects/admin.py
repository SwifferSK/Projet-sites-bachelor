from django.contrib import admin
from bachelor_projects.models import Project

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)


# Register your models here.
