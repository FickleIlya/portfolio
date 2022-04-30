from django.shortcuts import render
from .models import Project


# Create your views here.
def homepage(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'portfolio_templates/homepage.html', context=context)
