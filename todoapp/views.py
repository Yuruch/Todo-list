from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from todoapp.models import Task, Tag


class TaskListView(generic.ListView):
    queryset = Task.objects.prefetch_related("tag")
    fields = "__all__"
    template_name = "todoapp/home.html"


class TagListView(generic.ListView):
    model = Tag
    fields = "__all__"

