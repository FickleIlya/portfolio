from django.views.generic import ListView, TemplateView

from .models import Project


class HomepageView(TemplateView):
    template_name = "portfolio_templates/homepage.html"


class ProjectsListView(ListView):
    model = Project
    template_name = "portfolio_templates/projects.html"
    context_object_name = "projects"

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Project.objects.all()


class ContactView(TemplateView):
    template_name = "portfolio_templates/contacts.html"
