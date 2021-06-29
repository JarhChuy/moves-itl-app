# blog/views.py
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from .models import Post, Comment

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogAccionView(ListView):
    model = Post
    template_name = 'accion.html'
    
    # def get_queryset(self):
    #     return Post.objects.filter(id=1)

class BlogTerrorView(ListView):
    model = Post
    template_name = 'terror.html'

class BlogInfantilView(ListView):
    model = Post
    template_name = 'infantiles.html'
    
class BlogRomanticView(ListView):
    model = Post
    template_name = 'romanticas.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.autor != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['titulo', 'cuerpo','imagen','genero']

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.autor != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.autor != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class BlogAboutView(TemplateView):
    # model = Post
    template_name = 'about.html'

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment_new.html'
    fields = ('comment',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        v = self.request.META['HTTP_REFERER']
        x = v.split('/')
        form.instance.post = Post.objects.get(pk=x[4])
        return super().form_valid(form)

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'


    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.autor != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)