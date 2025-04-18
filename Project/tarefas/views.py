from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .forms import TarefaForm
from .models import TarefaModel


def tarefas_home(request):
    contexto = {"nome": "Lucas", "tarefas": TarefaModel.objects.all()}
    return render(request, "tarefas/home.html", contexto)


def tarefas_add(request: HttpRequest):
    if request.method == "POST":
        formulario = TarefaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("tarefas:home")

    contexto = {"form": TarefaForm}
    return render(request, "tarefas/add.html", contexto)


def tarefas_remove(request: HttpRequest, id):
    tarefa = get_object_or_404(TarefaModel, id=id)
    tarefa.delete()
    return redirect("tarefas:home")


def tarefas_edit(request: HttpRequest, id):
    tarefa = get_object_or_404(TarefaModel, id=id)
    if request.method == "POST":
        formulario = TarefaForm(request.POST, instance=tarefa)
        if formulario.is_valid():
            formulario.save()
            return redirect("tarefas:home")

    formulario = TarefaForm(instance=tarefa)
    contexto = {"form": formulario}
    return render(request, "tarefas/edit.html", contexto)
