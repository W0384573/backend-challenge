from django.shortcuts import render

from django.shortcuts import render
from .models import Task, Label

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def create_task(request):


def update_task(request, pk):


def delete_task(request, pk):
