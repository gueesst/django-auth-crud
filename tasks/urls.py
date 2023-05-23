from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("signup/", signup, name="signup"),
    path("tasks/", tasks, name="tasks"),
    path("tasks_completed/", tasks_completed, name="tasks_completed"),
    path("logout/", sigout, name="logout"),
    path("signin/", signin, name="login"),
    path("task/create/", create_task, name="create_task"),
    path("task/<int:task_id>/", task_detail, name="task_detail"),
    path("task/<int:task_id>/completed", complete_task, name="complete_task"),
    path("task/<int:task_id>/delete", delete_task, name="delete_task"),
]
