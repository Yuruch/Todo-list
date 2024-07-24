from django.contrib import admin
from django.urls import path

from todoapp.views import (
    TaskListView,
    TagListView,
    toggle_complete_task
)

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path(
        "tasks/<int:pk>/toggle-complete",
        toggle_complete_task,
        name="toggle-complete-task"
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name = "todo"
