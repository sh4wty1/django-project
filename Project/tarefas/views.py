from django.shortcuts import render
from django.http import HttpResponse


def tarefas_home(request):
    return HttpResponse("<h1>Aqui estão suas tarefas!!</h1>")
