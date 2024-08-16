from django.db import models
#
from django.views.generic import FormView, View
#
from applications.users.models import User
#
from model_utils.models import TimeStampedModel
# Create your models here.


class Post(TimeStampedModel):
    title = models.CharField('Titulo post', max_length=30)
    content = models.TextField('Contenido post')
    image = models.ImageField('Imagen', upload_to='ImagenPost', blank=True, null=True)
    user = models.ForeignKey(User, related_name='post_user', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    

    def __str__(self):
        return self.title
