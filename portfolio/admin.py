from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'updated_on')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
