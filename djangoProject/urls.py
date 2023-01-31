from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def projects(request):
    return HttpResponse('here our projects')


def homepage(request):
    return HttpResponse('HOMEPAGE')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', projects),
    path('', homepage),
    
]
