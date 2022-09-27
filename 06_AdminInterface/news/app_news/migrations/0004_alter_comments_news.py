# Generated by Django 4.1.1 on 2022-09-24 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0003_alter_comments_options_comments_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='news',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app_news.news', verbose_name='Новость'),
        ),
    ]
