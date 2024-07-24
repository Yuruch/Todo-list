from django.contrib import admin
from django.urls import path

from todoapp.views import TaskListView, TagListView

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name = "todo"
