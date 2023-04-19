from django.shortcuts import render
from .models import Post


posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2020'
    },
    {
        'author': 'Mary',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2020'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, template_name='blog/home.html', context=context)


def about(request):
    return render(request, template_name='blog/about.html', context={'title': 'About'})

