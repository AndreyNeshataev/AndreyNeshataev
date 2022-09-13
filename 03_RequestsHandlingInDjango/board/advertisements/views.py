from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


def advertisements(request, *args, **kwargs):
    return render(request, 'advertisements/advertisements.html', {})


class Advertisements(TemplateView):
    template_name = 'advertisements/advertisements.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'ГЛАВНАЯ СТРАНИЦА'
        context['title'] = 'Главная страница'
        context['advertisement'] = 'Страница с объявлениями'
        context['advertisement_url'] = '/advertisements'
        context['contacts'] = 'Контакты'
        context['contacts_url'] = '/contacts'
        context['about'] = 'Описание'
        context['about_url'] = '/about'
        context['categories'] = 'Категории'
        context['categories_url'] = '/categories'
        context['regions'] = 'Регионы'
        context['regions_url'] = '/regions'

        return context


class ListAdvertisements(View):
    count = 0

    def get(self, request):
        title = 'Список объявлений'
        name = 'ОБЪЯВЛЕНИЯ'
        advertisements = [
            'Мастер на час',
            'Выведение из запоя',
            'Услуги экскаватора-погрузчика, гидромолота, ямобура',
            'Ремонт бытовой техники',
            'Грузчики, помощь при переезде'
        ]
        return render(request, 'advertisements/advertisement_list.html', {'name': name,
                                                                          'title': title,
                                                                          'advertisements': advertisements})

    def post(self, request):
        message = 'Запрос на создание новой записи успешно выполнен'
        return render(request, 'advertisements/advertisement_list.html', {'message': message})


class Contacts(TemplateView):
    template_name = 'advertisements/contacts_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Контакты'
        context['title'] = 'Контакты'
        context['phone'] = 'Номер телефона: 8-800-708-19-45'
        context['mail'] = 'Email: sales@company.com'
        context['address'] = 'Адрес: г.Пермь, ул.Островского, 8'

        return context


class About(TemplateView):
    template_name = 'advertisements/about_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = """ООО "GENERIC" 
                          Бесплатные объявления в вашем городе"""
        context['title'] = 'Бесплатные объявления'
        context['description'] = """
                      Универсальный сайт для размещения бесплатных объявлений в любой категории товаров и услуг. 
                      Можно размещать неограниченное количество объявлений бесплатно. 
                      Доски бесплатных объявлений в России на сайте. 
                      Популярная барахолка, частные объявления в России без регистрации. 
                      Разместить своё объявление бесплатно, быстро, купить, продать без посредников у частных лиц"""
        return context


class Categories(TemplateView):
    template_name = 'advertisements/categories_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'КАТЕГОРИИ'
        context['title'] = 'Категории'
        context['categories'] = ['Личные вещи', 'Транспорт', 'Хобби и отдых', 'Недвижимость', 'Работа', 'Электроника']

        return context


class Regions(View):
    def get(self, request):
        regions = ['Москва', 'Московская область', 'Pеспублика Алтай', 'Вологодская область']
        return render(request, 'advertisements/regions_list.html', {'regions': regions})

    def post(self, request):
        message = 'Регион успешно создан'
        return render(request, 'advertisements/regions_list.html', {'message': message})
