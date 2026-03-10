from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

# Create your views here.
def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form = UserCreationForm()
  
  return render(request, 'register.html', {'form': form})

def index(request):
  return render(request, 'index.html')

@login_required
def task_list(request):
  tasks = Task.objects.filter(user=request.user)
  return render(request, 'task_list.html', {'tasks':tasks})

@login_required
def task_create(request):
  form = TaskForm(request.POST or None)
  if form.is_valid():
    task = form.save(commit=False)
    task.user = request.user
    task.save()
    return redirect('task_list')
  return render(request, 'task_form.html', {'form': form})

@login_required
def task_update(request, pk):
  task = Task.objects.get(pk=pk)
  if task.user != request.user:
    return redirect('task_list')
  form = TaskForm(request.POST or None, instance=task)
  if form.is_valid():
    form.save()
    return redirect('task_list')
  return render(request, 'task_form.html', {'form':form})

@login_required
def task_delete(request, pk):
  task = Task.objects.get(pk=pk)
  if task.user == request.user:
    task.delete()
  return redirect('task_list')