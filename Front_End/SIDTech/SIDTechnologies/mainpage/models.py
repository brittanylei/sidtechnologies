from django.db import models

from .forms import ProjectForm


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNum = models.CharField(max_length=15)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Sprint(models.Model):
    projectName = models.CharField(max_length=50)
    projectOwner = models.CharField(max_length=50)
    scrumMaster = models.CharField(max_length=50)
    team = models.CharField(max_length=50)
    sprintNum = models.IntegerField(default=0)
    sprintPlanDate = models.DateTimeField()
    sprintRevDate = models.DateTimeField()
    sprintRetroDate = models.DateTimeField()
    scrumMeetDate = models.DateTimeField()

    def __str__(self):
        return self.projectName

    # write a function to write form data to this class
