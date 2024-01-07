from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.db.models import Q

def home(request):
    """View function for home page of site."""
    # Render the HTML template index.html with the data in the context variable
    data = Task.objects.all()
    return render(request, 'all.html', context={'tasks':data})


def add(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            title=request.POST['title']
            body=request.POST['body']
            new_task = Task(title=title, body=body)
            new_task.save()
            return redirect('home')
    return render(request, 'add.html', {"form":form})


def search(request, name):
    task = Task.objects.filter(Q(title__icontains=name) | Q(body__icontains=name))
    if len(task) >= 0:
        context = {"tasks":task}
        return render(request, 'all.html',context=context)
    else:
        context= {}
        return render(request, 'all.html', context=context)


def delete(request, pk):
    Task.objects.filter(id=pk).delete()
    return redirect("home")


def detail(request, id):
    task = Task.objects.get(id=id)
    context= {"task":task}
    return render(request, 'detail.html', context=context)