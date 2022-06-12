from django.urls import path

from api.views import *

urlpatterns = [

    # API blogs
    path('bloglist/', BlogAPIListCreate.as_view()),
    path('bloglist/<int:pk>', BlogAPIRCD.as_view()),

    # API projects
    path('projectlist/', ProjectAPIListCreate.as_view()),
    path('projectlist/<int:pk>', ProjectAPIRCD.as_view()),

]
