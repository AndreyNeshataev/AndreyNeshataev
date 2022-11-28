# Generated by Django 4.1.1 on 2022-11-18 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_marketplace', '0006_price_quantity_remove_goods_variables_goods_shop_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_marketplace.price', verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='quantity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_marketplace.quantity', verbose_name='Количество'),
        ),
    ]
