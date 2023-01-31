from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    return HttpResponse('here our projects')


def project(request, pk):
    return HttpResponse('here our projects' + ' ' + pk)

# Create your views here.
