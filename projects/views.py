from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    return render(request, 'projects/html/projects.html')


def project(request, pk):
    return render(request, 'projects/html/single-project.html')

# Create your views here.
