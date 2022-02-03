# Add your Views Here
from django.shortcuts import render
from django.http import HttpResponseRedirect
from tasks.models import Task


def tasks_view(request):
    pending = Task.objects.filter(deleted=False, completed=False)
    return render(request, "tasks.html", {"tasks": pending})


def add_task(request):
    task = request.GET.get("task")
    Task(title=task).save()
    return HttpResponseRedirect("/tasks")


def complete_task(request, index):
    Task.objects.filter(id=index).update(completed=True)
    return HttpResponseRedirect("/tasks")


def delete_task(request, index):
    Task.objects.filter(id=index).update(deleted=True)
    return HttpResponseRedirect("/tasks")


def completed_tasks(request):
    completed = Task.objects.filter(completed=True)
    return render(request, "allTasks.html", {"completed": completed})


def allTasks(request):
    pending = Task.objects.filter(deleted=False, completed=False)
    completed = Task.objects.filter(completed=True)
    return render(request, "allTasks.html", {"completed": completed, "tasks": pending})
