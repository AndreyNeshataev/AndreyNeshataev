from django.db import models
from django.urls import reverse


class News(models.Model):
    ACTIVITY_FLAG_CHOICES = [
        ('a', 'Активно'),
        ('i', 'Неактивно')
    ]

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    # slug = models.SlugField(max_length=255, unique=True, null=True, db_index=True, verbose_name="URL")
    article = models.CharField(max_length=1500, default='', verbose_name='Статья')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    activity_flag = models.CharField(max_length=10, default='i',
                                     choices=ACTIVITY_FLAG_CHOICES, verbose_name="Активность")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])

    # def get_absolute_url(self):
    #     return reverse('news', kwargs={'news_slug': self.slug})

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        db_table = 'News'
        ordering = ['-created_date', 'title']


class Comments(models.Model):
    user_name = models.CharField(max_length=100, db_index=True, verbose_name='Имя пользователя')
    commentary = models.CharField(max_length=500, verbose_name='Комментарий')
    created_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')
    news = models.ForeignKey('News', on_delete=models.CASCADE, blank=True, null=True,
                             related_name='comments', verbose_name='Новость')

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'
        db_table = 'comments'
        ordering = ['-created_date']
