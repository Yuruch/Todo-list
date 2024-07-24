from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False, blank=True)
    tag = models.ManyToManyField("Tag", related_name="tasks")


class Tag(models.Model):
    name = models.CharField(max_length=255)
