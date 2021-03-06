# blog/urls.py

from django.urls import path

from .views import (
  BlogListView, 
  BlogAccionView, 
  BlogTerrorView, 
  BlogInfantilView, 
  BlogRomanticView, 
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
    path('post/<int:pk>/deleteComment/', CommentDeleteView.as_view(), name='comment_delete' ),
    path('about/', BlogAboutView.as_view(), name='about'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>', BlogDetailView.as_view(), name='post_detail'),
    path('romanticas', BlogRomanticView.as_view(), name='romanticas'),
    path('infantil', BlogInfantilView.as_view(), name='infantil'),
    path('terror', BlogTerrorView.as_view(), name='terror'),
    path('accion', BlogAccionView.as_view(), name='accion'),
    path('', BlogListView.as_view(), name='home'),
]
