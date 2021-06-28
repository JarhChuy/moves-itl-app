from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    cuerpo = models.TextField("Descripcion")
    imagen = models.CharField( "Imagen link", max_length=500 )
    
    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class Comment(models.Model):
    post = models.ForeignKey(#user)
        Post,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    comment = models.CharField(max_length=140)
    autor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.post.id)])
        # return reverse('component_list') 

    
    def get_success_url(self):
          # if you are passing 'pk' from 'urls' to 'DeleteView' for company
          # capture that 'pk' as companyid and pass it to 'reverse_lazy()' function
          return reverse_lazy('post_detail', kwargs={'id': self.post.id})

