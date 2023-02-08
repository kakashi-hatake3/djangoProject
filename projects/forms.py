from django.forms import ModelForm
from .models import Project


class ProjectsForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'demo_link', 'source_link', 'tags']
