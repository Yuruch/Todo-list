from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False, blank=True)
    tag = models.ManyToManyField("Tag", related_name="tasks")

    class Meta:
        ordering = ("status", "-created_at")

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
