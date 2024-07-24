from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todoapp.models import Task, Tag


class TaskListView(generic.ListView):
    queryset = Task.objects.prefetch_related("tag")
    fields = "__all__"
    template_name = "todoapp/home.html"


class TagListView(generic.ListView):
    model = Tag
    fields = "__all__"


def toggle_complete_task(request: HttpRequest, pk: int) -> HttpResponse:
    task = Task.objects.get(pk=pk)
    task.status = not task.status
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo:home"))
