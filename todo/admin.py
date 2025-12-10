from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'priority', 'status', 'due_date', 'completed', 'created')
    list_filter = ('priority', 'status', 'completed', 'created')
    search_fields = ('title', 'description', 'user__username')
    date_hierarchy = 'created'
    ordering = ('-created',)