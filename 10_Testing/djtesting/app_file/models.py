from django.db import models
from datetime import datetime
from blog.models import Post


# Create your models here.

def user_directory_path(instance, filename):
    path = f'files/{datetime.now().strftime("%d_%m_%y-%H-%M-%S")}_{filename}'
    return path


class AppFile(Post):
    file = models.FileField(upload_to=user_directory_path, null=True, blank=True,
                            verbose_name='Файл')

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

