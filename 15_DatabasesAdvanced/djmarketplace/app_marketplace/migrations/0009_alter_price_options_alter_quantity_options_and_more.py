# Generated by Django 4.1.1 on 2022-11-18 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_marketplace', '0008_rename_price_price_value_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='price',
            options={'verbose_name': 'Цена', 'verbose_name_plural': 'Цены'},
        ),
        migrations.AlterModelOptions(
            name='quantity',
            options={'verbose_name': 'Количество', 'verbose_name_plural': 'Количество'},
        ),
        migrations.AlterModelOptions(
            name='variation',
            options={'verbose_name': 'Вариация', 'verbose_name_plural': 'Вариации'},
        ),
        migrations.AddField(
            model_name='variation',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_marketplace.marketplace', verbose_name='Магазин'),
        ),
        migrations.AlterField(
            model_name='price',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Цена товара'),
        ),
        migrations.AlterField(
            model_name='quantity',
            name='value',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Количество товара'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='goods',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='variations', to='app_marketplace.goods', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='price',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app_marketplace.price', verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='quantity',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app_marketplace.quantity', verbose_name='Количество'),
        ),
    ]
