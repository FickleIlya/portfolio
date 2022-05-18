from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [

    path('', views.homepage, name='home'),
    path('linkedin/', views.linkedin, name='linkedin'),
    path('contacts/', views.contacts, name='contacts'),

]
