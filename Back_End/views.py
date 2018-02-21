from django.shortcuts import render, get_object_or_404
from forms import UserForm
# from django.contrib.models import User
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from sid.models import Client, Sprint

# def get_sprintNum(request, sprint_id):
#     if request.method == 'GET':
#         data =
#         return render(request, template_name='.html')
#
#     elif request.method == 'POST':
#         data =

# # Project Backlog
# def proj_backlog(request):
#
#     return render(request, 'project_backlog.html', {:})
#
# def proj_goals(request):
#
# def proj_us(request):
#
#
# # Sprint Backlog
# def sprint_backlog(request):
#
# def spring_goals(request):
#
# def sprint_us(request):
#
# def spring_tasks(request):
#
#
# # Scrum Board
# def scrum_board(request):
#
# def to_do(request):
#
# def in_progress(request):
#
# def completed(request):
#
# 
# # Burn-up Chart
#
# def burn_chart(request):
#

# def create_user(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             new_user = User.objects.create_user(**form.cleaned_data)
#             login(new_user)
#             return HttpResponseRedirect('main.html')
#     else:
#         form = UserForm()
#
#     return render(request, 'adduser.html', {'form':form})
