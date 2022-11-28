import random
import datetime
from django.utils.translation import gettext_lazy as _
from app_marketplace.models import Variation


def sale():
    variation_list = Variation.objects.select_related('shop').all()
    today = datetime.date.today()
    sale_date = variation_list.first().shop.sale_date
    days = [_("Понедельник"), _("Вторник"), _("Среда"), _("Четверг"), _("Пятница"), _("Суббота"), _("Воскресенье")]
    day_number = datetime.date.today().weekday()
    day = days[day_number]
    right_day = False
    if day_number in [4, 5, 6]:
        right_day = True
    if sale_date != today:
        for var in variation_list:
            if day_number in [5, 6]:
                var.sale = random.randrange(2, 30, 5)
            elif day_number == 4:
                var.sale = random.randrange(2, 10, 2)
            else:
                var.sale = 0
            var.save()
            var.shop.sale_date = datetime.date.today()
            var.shop.save()
    return right_day, day

