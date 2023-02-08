from django.forms import ModelForm
from .models import Project


class ProjectsForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
