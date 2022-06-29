from django.shortcuts import render
from .models import Project


def homepage(request):
    return render(request, 'portfolio_templates/homepage.html')


def projects(request):
    projects = Project.objects.all()

    context = {
        'projects': projects,
    }
    return render(request, 'portfolio_templates/projects.html', context=context)


def contacts(request):
    return render(request, 'portfolio_templates/contacts.html')