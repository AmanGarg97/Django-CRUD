from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


# Create your views here.
def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tag = projectObj.tags.all()
    context = {'project': projectObj, 'tags': tag}
    return render(request, 'projects/project.html', context)

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    form = ProjectForm()
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

def update_project(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, project)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    form = ProjectForm(instance=project)
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()
    return redirect('projects')
