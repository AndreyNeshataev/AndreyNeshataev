# Generated by Django 4.1.1 on 2022-09-27 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0009_alter_comments_commentary_alter_news_activity_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='commentary',
            field=models.CharField(choices=[('d', 'Удалено администратором')], max_length=500, verbose_name='Комментарий'),
        ),
    ]
