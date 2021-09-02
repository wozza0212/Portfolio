from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})


def about_me(request):
    return render(request, 'portfolio/about_me.html')


def contact_me(request):
    return render(request, 'portfolio/contact_me.html')


def skills(request):
    return render(request, 'portfolio/skills.html')


def projects(request):
    return render(request, 'portfolio/projects.html')
