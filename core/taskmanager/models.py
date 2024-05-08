from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from simple_history.models import HistoricalRecords
from .enums import Priority, Status


class Category(models.Model):
    name = models.CharField(_("Category"), max_length=50)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    name = models.CharField(_("name"), max_length=255)
    description = models.TextField(_("description"), max_length=1000)
    deadline = models.DateField(_("deadline"), auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(
        _("created at"), auto_now=False, auto_now_add=True
    )
    assignee = models.ManyToManyField(
        User,
        verbose_name=_("assignee"),
        related_name="tasks_assigned_to",
    )
    assignor = models.ForeignKey(
        User,
        verbose_name=_("assignor"),
        on_delete=models.DO_NOTHING,
        related_name="tasks_assigned_by",
    )
    status = models.CharField(
        _("status"), choices=Status.choices, default=Status.TODO, max_length=11
    )
    priority = models.IntegerField(
        _("priority"), choices=Priority.choices, default=Priority.HIGH
    )
    category = models.ForeignKey(
        "taskmanager.Category", verbose_name=_(""), on_delete=models.CASCADE, null=True
    )
    history = HistoricalRecords()

    class Meta:
        ordering = ["deadline"]

    def __str__(self) -> str:
        return self.name

    def assignees(self) -> models.QuerySet:
        return self.assignee

    def assignors(self) -> User:
        return self.assignor
