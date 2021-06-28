# blog/urls.py

from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogAboutView#, CommentCreateView, CommentDeleteView,

from .views import (
  BlogListView, 
  BlogDetailView, 
  BlogCreateView, 
  BlogUpdateView,
  BlogDeleteView,
  BlogAboutView,
  CommentCreateView,
  CommentDeleteView,
)

urlpatterns = [
    path('post/<int:pk>/newComment', CommentCreateView.as_view(), name='comment_new'),
    # path('comment/<int:pk>/new', CommentCreateView.as_view(), name='comment_new'),
    path('post/<int:pk>/deleteComment/', CommentDeleteView.as_view(), name='comment_delete' ),
    path('about/', BlogAboutView.as_view(), name='about'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]