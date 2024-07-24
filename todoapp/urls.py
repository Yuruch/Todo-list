from django.contrib import admin
from django.urls import path

from todoapp.views import TaskListView

urlpatterns = [
    path("home/", TaskListView.as_view(), name="home"),
]

app_name = "todo"
