# Generated by Django 4.1.1 on 2022-09-27 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0007_alter_news_activity_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='activity_flag',
            field=models.CharField(choices=[('a', 'active'), ('i', 'inactive')], default=False, max_length=10, verbose_name='Активность'),
        ),
    ]
