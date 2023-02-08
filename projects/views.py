from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Review, Tag
from .forms import ProjectsForm


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/html/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/html/single-project.html', {'project': projectObj})


def createProject(request):
    form = ProjectsForm()
    context = {'form': form}
    return render(request, 'projects/html/project_form.html', context)
