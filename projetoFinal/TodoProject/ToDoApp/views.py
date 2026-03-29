from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm, BootstrapUserCreationForm

# Create your views here.
def register(request):
  if request.method == 'POST':
    form = BootstrapUserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form = BootstrapUserCreationForm()
  
  return render(request, 'register.html', {'form': form})

def logout_view(request):
  logout(request)
  return redirect('login')

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