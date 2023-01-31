from django.shortcuts import render
from django.http import HttpResponse

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
    page = 'projects'
    number = 9
    context = {'page': page, 'number': number, 'projects': projectslist}
    return render(request, 'projects/html/projects.html', context)


def project(request, pk):
    projectObj = None
    for i in projectslist:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/html/single-project.html', {'project': projectObj})

# Create your views here.
