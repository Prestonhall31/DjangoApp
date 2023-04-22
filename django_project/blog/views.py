from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


# Code was refactored below
# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, template_name='blog/home.html', context=context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<modle>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user # Setting the instance to the current logged in user.
        return super().form_valid(form)


def about(request):
    return render(request, template_name='blog/about.html', context={'title': 'About'})


