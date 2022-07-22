from django.urls import path
from .views import ProjectsListView, HomepageView, ContactView

app_name = 'portfolio'

urlpatterns = [

    path('', HomepageView.as_view(), name='home'),
    path('projects/', ProjectsListView.as_view(), name='projects'),
    path('contacts/', ContactView.as_view(), name='contacts'),

]
