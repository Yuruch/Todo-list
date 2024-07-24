from django.contrib import admin
from django.urls import path

from todoapp.views import (
    TaskListView,
    TagListView,
    toggle_complete_task,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path(
        "tasks/<int:pk>/toggle-complete",
        toggle_complete_task,
        name="toggle-complete-task"
    ),
    path(
        "tasks/<int:pk>/update",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name = "todo"
