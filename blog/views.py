# blog/views.py
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .models import Post

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

# class BlogListView(TemplateView):
#     template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['titulo', 'cuerpo','imagen']

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

# class CommentCreateView(LoginRequiredMixin, CreateView):
#     model = Comment
#     template_name = 'comment_new.html'
#     fields = ('comment',)
#     login_url = 'login'

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         v = self.request.META['HTTP_REFERER']
#         x = v.split('/')
#         form.instance.component = Component.objects.get(pk=x[4])
#         return super().form_valid(form)

# class CommentDeleteView(LoginRequiredMixin, DeleteView):
#     model = Comment
#     template_name = 'comment_delete.html'
#     success_url = reverse_lazy('component_list')
#     login_url = 'login'

#     def dispatch(self, request, *args, **kwargs):
#         obj = self.get_object()
#         if obj.author != self.request.user:
#             raise PermissionDenied
#         return super().dispatch(request, *args, **kwargs)