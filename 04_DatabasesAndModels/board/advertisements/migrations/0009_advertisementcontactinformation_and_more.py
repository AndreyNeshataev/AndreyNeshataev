# Generated by Django 4.1.1 on 2022-09-14 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0008_remove_advertisement_author_contact_info_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisementContactInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=12)),
            ],
        ),
        migrations.AddField(
            model_name='advertisement',
            name='author_contact_info',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='advertisements.advertisementcontactinformation', verbose_name='Контакты автора'),
        ),
    ]