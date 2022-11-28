from django.core.management.base import BaseCommand
from app_marketplace.models import Goods


class Command(BaseCommand):
    help = 'Удалить статьи'

    def handle(self, *args, **options):
        goods = Goods.objects.all()[5:]
        for good in goods:
            good.delete()
        goods = Goods.objects.all()
        self.stdout.write(f'Статьи успешно удалены. Остались: {goods}')