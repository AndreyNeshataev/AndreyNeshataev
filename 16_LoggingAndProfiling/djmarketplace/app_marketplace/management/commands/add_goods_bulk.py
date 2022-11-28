from django.core.management.base import BaseCommand
from app_marketplace.models import Marketplace, Goods, Variation
import time
import random


class Command(BaseCommand):
    help = 'Добавить статьи'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Количество создаваемых товаров')

    def handle(self, *args, **kwargs):
        t0 = time.time()
        total = kwargs['total'] + 6
        # goods = Goods.objects.only('name').first()
        # shop = Marketplace.objects.get(id=random.randint(1, 3))
        goods_to_insert = [Variation(product=Goods.objects.create(name_goods=f'Товар {i}',
                                                                  description=f'Товар {i} тест {i}'),
                                     quantity=random.randint(10, 30),
                                     price=random.randint(10, 30) * 10,
                                     sale=random.randint(2, 10),
                                     shop=Marketplace.objects.get(id=random.randint(1, 3))
                                     ) for i in range(6, total)]
        Variation.objects.bulk_create(goods_to_insert)
        t1 = time.time()
        self.stdout.write(f'Статьи успешно созданы. Время работы программы: {t1 - t0}')
