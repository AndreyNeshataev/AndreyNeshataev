from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from time import time
from django.contrib.auth.models import User


# Create your models here.
def generate_slug(string):
    new_slug = slugify(string, allow_unicode=True)
    new_slug += '-' + str(int(time()))
    return new_slug


class Post(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name=_('Заголовок'))
    slug = models.SlugField(max_length=50, blank=True, unique=True, verbose_name='URL')
    article = models.CharField(max_length=1500, blank=True, verbose_name=_('Текст статьи'))
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    updated_date = models.DateTimeField(auto_now=True, verbose_name=_('Дата изменения'))
    published = models.BooleanField(default=False, verbose_name=_("Опубликовано"))
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts', verbose_name=_("Теги"))
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,
                               null=True, verbose_name=_("Пользователь"))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = generate_slug(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Статья')
        verbose_name_plural = _('Статьи')
        db_table = 'post'
        ordering = ['-created_date', 'title']


class PostImage(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, blank=True, null=True,
                             verbose_name=_('Статья'))
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name=_("Фотография"))

    class Meta:
        verbose_name = _('Фотография')
        verbose_name_plural = _('Фотографии')


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name=_("Тег"))
    slug = models.SlugField(max_length=50, unique=True, verbose_name="URL")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = _('Тег')
        verbose_name_plural = _('Теги')
        ordering = ['title']
