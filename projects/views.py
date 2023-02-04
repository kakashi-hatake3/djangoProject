from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Review, Tag


projectslist = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'On this website you can see all my projects'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'Awesome open source project'
    },
]


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/html/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/html/single-project.html', {'project': projectObj})

# Create your views here.
