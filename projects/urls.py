from django.urls import path
from . import views


urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>/', views.project),
    path('create_project/', views.createProject),
    path('update_project/<str:pk>/', views.updateProject, name='update_project'),
    path('delete_project/<str:pk>/', views.deleteProject, name='delete_project'),

]
