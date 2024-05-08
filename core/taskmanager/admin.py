from django.contrib import admin

from .models import Task

# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "assignor",
        "get_assignees",
        "deadline",
        "status",
        "priority",
    )
    list_filter = ("status", "priority", "deadline", "category")
    search_fields = ("name", "assignor__username", "assignee__username")

    def get_assignees(self, obj):
        return ",".join([assignee.username for assignee in obj.assignee.all()])

    get_assignees.short_description = "Assignees"
