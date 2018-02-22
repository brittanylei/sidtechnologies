from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader

from .forms import ProjectForm
from .models import *
def index(request):
    template = loader.get_template('mainpage/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def redirect(request):
    template = loader.get_template('mainpage/page2.html')

    return HttpResponse(template.render({}, request))

def getProject(request):
 # if this is a POST request we need to process the form data
    template = loader.get_template('mainpage/getProject.html')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # perhaps store data into database
            # redirect to a new URL:
            # return HttpResponseRedirect('/page2/')
            # ...
            project = ProjectForm.save(commit=False)
            store = Store.Objects.get(store_name=store_name)
            project.store = store
            project.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProjectForm()

    return HttpResponse(template.render({'form':form}, request))
