from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import BlogForm
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog_templates/blogs.html', context=context)


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'blog_templates/detail.html', context=context)


@login_required
def create_blog(request):
    context = {
        'form': BlogForm()
    }
    if request.method == 'GET':

        return render(request, 'blog_templates/create_blog.html', context=context)

    elif request.method == 'POST':
        try:
            form = BlogForm(request.POST)
            new_blog = form.save(commit=False)
            new_blog.user = request.user
            new_blog.save()
            return redirect('blog:all_blogs')
        except ValueError:
            context['error'] = 'Too much symbols'
            return render(request, 'blog_templates/create_blog.html', context=context)


@login_required
def change_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        'blog': blog
    }
    if request.method == 'GET':
        form = BlogForm(instance=blog)
        context['form'] = form
        return render(request, 'blog_templates/change_blog.html', context=context)
    elif request.method == 'POST':

        try:
            form = BlogForm(request.POST, instance=blog)
            form.save()
            return redirect('blog:detail', blog_id=blog_id)
        except ValueError:
            context['error'] = 'Bad info'
            return render(request, 'blog_templates/change_blog.html', context=context)


@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    if request.method == "POST":
        blog.delete()
        return redirect("blog:all_blogs")
