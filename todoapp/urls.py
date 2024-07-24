from django.contrib import admin
from django.urls import path

from todoapp.views import (
    TaskListView,
    TagListView,
    toggle_complete_task,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagUpdateView,
    TagDeleteView,
    TagCreateView,
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
    path(
        "tags/<int:pk>/update",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tags/<int:pk>/delete",
        TagDeleteView.as_view(),
        name="tag-delete"
    ),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create"
    ),
]

app_name = "todo"
