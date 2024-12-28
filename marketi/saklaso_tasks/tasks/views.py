from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


def home(request):
    name = request.GET.get('name')
    status = request.GET.get('status')
    description = request.GET.get('description')





    return render(request, 'home.html')

def create_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES )
        if form.is_valid():
            form.save




    return render(request, 'task_form.html')

def update_task(request,pk):
    Task = get_object_or_404(Task, id=id)
    form = TaskForm(instance=Task)
    if request.method == 'POST':
        form = TaskForm(request.POST,request.FILES,instance = Task)
        if form.is_valid:
            form.save
            return redirect('home')
        

    return render(request, 'task_form.html')


def delete_task(request, pk):
    Task = get_object_or_404(Task,id=id)
    Task.delete()

    return redirect('home')

def detail_task(request, pk):
    Task = get_object_or_404(Task, id=id)
    return render(request, 'task_detail.html')