# Generated by Django 4.1.1 on 2022-11-04 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_shops', '0002_alter_goods_price_alter_shop_sale_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shop_goods', to='app_shops.shop', verbose_name='Магазин'),
        ),
        migrations.CreateModel(
            name='StoreOffers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.CharField(max_length=500, verbose_name='Предложение магазина')),
                ('shop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shop_offers', to='app_shops.shop', verbose_name='Магазин')),
            ],
            options={
                'verbose_name': 'Предложение магазина',
                'verbose_name_plural': 'Предложения магазина',
            },
        ),
    ]