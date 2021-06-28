from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    imagen = models.CharField( "Imagen link", max_length=500 )
    cuerpo = models.TextField("Descripcion")

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])