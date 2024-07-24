from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from todoapp.models import Task


class TaskListView(generic.ListView):
    queryset = Task.objects.prefetch_related("task")
    fields = "__all__"
    template_name = "Home"
