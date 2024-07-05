from django.shortcuts import render, redirect
from django.urls import reverse

from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .models import Task
from .forms import TaskForm
# Project Views:
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

## CRUD Operations
## Funcion-based Views

# Read
def view_tasks(request):
    tasks = Task.objects.all().values()

    context = {
        'tasks': tasks,
               }
    return render(request, 'todo/view-tasks.html', context)

# Create
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('todo:view-tasks'))
    else:
        form = TaskForm()
    context = {
        'form': form,
         }

    return render(request, 'todo/create-update-task.html', context)

# Update
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(reverse('todo:view-tasks'))
    else:
        form = TaskForm(instance = task)
    context = {
           'form': form,
'task': task,
        }

    return render(request, 'todo/create-update-task.html', context)

# Delete
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect(reverse('todo:view-tasks'))

## Class-based Views
# Create
class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'due', 'status']
    template_name = 'todo/create-update-task.html'
    success_url = '/todo'

# Read
class TaskListView(ListView):
    model = Task
    template_name = 'todo/view-tasks.html'
    context_object_name = 'tasks'

# Update
class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'due', 'status']
    template_name = 'todo/create-update-task.html'
    success_url = '/todo'

# Delete
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todo/confirm-delete-task.html'
    success_url = '/todo'
