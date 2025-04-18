from . import views
from django.contrib import admin
from django.urls import path, include

app_name = "tarefas"

urlpatterns = [
    path("", views.tarefas_home, name="home"),
    path("add/", views.tarefas_add, name="add"),
    path("remove/<int:id>", views.tarefas_remove, name="remove"),
    path("edit/<int:id>", views.tarefas_edit, name="edit"),
]
