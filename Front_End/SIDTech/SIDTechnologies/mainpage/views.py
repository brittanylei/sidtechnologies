from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template import loader

# from .forms import ProjectForm
from .models import *

def index(request):
    template = loader.get_template('mainpage/index.html')
    print ("\n")
    print (request.method)
    print ("\n")
    if request.method == 'GET':
        form = SprintForm(request.GET)
        # data = Sprint.objects.all()
        # sprints = {
        #     'sprint':data
        # }

        return HttpResponse(template.render({'form':form}, request))

    else:
        context = {

        }
        return HttpResponse(template.render(context, request))


def redirect(request):
    template = loader.get_template('mainpage/page2.html')

    return HttpResponse(template.render({}, request))

def getProject(request):
 # if this is a POST request we need to process the form data
    template = loader.get_template('mainpage/getProject.html')
    print ("\n")
    print (request.method)
    print ("\n")
    if request.method == 'GET':
        form = SprintForm()
        # create a form instance and populate it with data from the request:


    # if a GET (or any other method) we'll create a blank form
    else:
        form = SprintForm(request.POST)

        # check whether it's valid:

        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            project = SprintForm.save(commit=False)
            # project = SprintForm.objects.get()
            store = Store.Objects.get(store_name=store_name)
            project.store = store
            project.save()
            template = loader.get_template('mainpage/index.html')
            # redirect to a new URL:
            return HttpResponse(template.render({'form':form}, request))

    return HttpResponse(template.render({'form':form}, request))
