from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField('Название новости', max_length=200)
    summary = models.TextField('Краткое содержание')
    content = models.TextField('Новость')
    posted_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    #def __str__(self):
        #return self.title

