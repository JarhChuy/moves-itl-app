from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    cuerpo = models.TextField("Descripcion")
    imagen = models.CharField( "Imagen link", max_length=500 )
    
    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class Comentarios(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    comment = models.CharField(max_length=140)
    autor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('component_list') 

