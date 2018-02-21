from django.urls import path

from . import views

urlpatterns = [
    # ex: /mainpage/
    path('', views.index, name='index'),
    # ex: /mainpage/5/
    path('page2.html', views.redirect, name='page2'),
    path('getProject.html', views.getProject, name='getProject')
]
