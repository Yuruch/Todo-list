from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todoapp.forms import TaskForm
from todoapp.models import Task, Tag


class TaskListView(generic.ListView):
    queryset = Task.objects.prefetch_related("tag")
    fields = "__all__"
    template_name = "todoapp/home.html"


class TaskCreateView(generic.CreateView):
    form_class = TaskForm
    success_url = reverse_lazy("todo:home")
    template_name = "todoapp/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:home")
    template_name = "todoapp/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:home")


class TagListView(generic.ListView):
    model = Tag
    fields = "__all__"


def toggle_complete_task(request: HttpRequest, pk: int) -> HttpResponse:
    task = Task.objects.get(pk=pk)
    task.status = not task.status
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo:home"))


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:home")
    template_name = "todoapp/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:home")
    template_name = "todoapp/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:home")
