from django.shortcuts import render, HttpResponse


# Create your views here.
def homepage(request):
    context = {}
    return render(request, 'portfolio_templates/homepage.html', context=context)
