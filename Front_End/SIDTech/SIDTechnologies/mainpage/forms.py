from django import forms
from .models import *


class ProjectForm(forms.Form):
    owner = forms.CharField(label='Project Owner', max_length=100)
    scrummaster = forms.CharField(label='Scrum Master', max_length=100)
    devteam = forms.CharField(label='Development Team', max_length=100)
    sprint = forms.IntegerField(label='Sprint', min_value=1)
    sprintplan = forms.CharField(label='Sprint Planning Meeting')
    meeting1 = forms.CharField(label='Scrum Meeting 1')
    meeting2 = forms.CharField(label='Scrum Meeting 2')
    meeting3 = forms.CharField(label='Scrum Meeting 3')
    sprintreview = forms.CharField(label='Sprint Review Meeting')
    retrospective = forms.CharField(label='Retrospective')
