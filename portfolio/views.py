from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
# from .models import Blog


def home(request):
    projects = Project.objects.all()
   
    return render(request, 'portfolio/home.html', {'projects':projects})