# Generated by Django 4.1.2 on 2022-10-19 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postimage',
            options={'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
    ]