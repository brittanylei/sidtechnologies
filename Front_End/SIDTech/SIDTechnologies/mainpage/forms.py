from django import forms

class ProjectForm(forms.Form):
    owner = forms.CharField(label='Project Owner', max_length=100)
    scrummaster = forms.CharField(label='Scrum Master', max_length=100)
    devteam = forms.CharField(label='Development Team', max_length=100)
    sprint = forms.IntegerField(label='Sprint', min_value=1)
    sprintplan = forms.DateTimeField(label='Sprint Planning Meeting')
    meeting1 = forms.DateTimeField(label='Scrum Meeting 1')
    meeting2 = forms.DateTimeField(label='Scrum Meeting 2')
    meeting3 = forms.DateTimeField(label='Scrum Meeting 3')
    sprintreview = forms.DateTimeField(label='Sprint Review Meeting')
    retrospective = forms.DateTimeField(label='Retrospective')
