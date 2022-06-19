from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [

    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),

    path('create/', views.create_blog, name="create_blog"),
    path('<int:blog_id>/change', views.change_blog, name="change_blog"),
    path('<int:blog_id>/delete', views.delete_blog, name="delete_blog"),
]
