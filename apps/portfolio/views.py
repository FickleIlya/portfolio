from django.shortcuts import render
from .models import Project
import datetime as dt


# Create your views here.
def homepage(request):
    projects = Project.objects.all()
    today = dt.date.today()
    if today.day >= 4 and today.month >= 1:
        my_age = today.year % 1000
    else:
        my_age = (today.year % 1000) - 1
    context = {
        'my_age': my_age,
        'projects': projects,
    }
    return render(request, 'portfolio_templates/homepage.html', context=context)
