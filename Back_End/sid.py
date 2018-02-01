

from django.db import models

class Client(models.Model):
  name = model.CharField(max_length=100)
  email = model.EmailField()
  phoneNum = model.CharField(max_length=15)
  position = model.CharField(max_length=50)

  def __str__(self):
    return self.name


class Sprint(models.Model):
  projectName = model.CharField(max_length=50)
  projectOwner = model.CharField(max_length=50)
  scrumMaster = model.CharField(max_length=50)
  team = model.CharField(max_length=50)
  sprintNum = models.IntegerField(default=0)
  sprintPlanDate = models.DateTimeField()
  sprintRevDate = models.DateTimeField()
  sprintRetroDate = models.DateTimeField()
  scrumMeetDate = models.DateTimeField()
