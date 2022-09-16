from django.views import generic
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import *
import requests


menu = [{'title': 'Перейти к странице с объявлениями', 'url_name': 'advertisement'},
        {'title': 'Описание сайта', 'url_name': 'about'}]


def advertisement_list(request, *args, **kwargs):
    advertisements = Advertisement.objects.all()
    context = {'title': 'Главная страница',
               'header': 'Бесплатные объявления',
               'advertisements': advertisements,
               'menu': menu}
    return render(request, 'advertisements/advertisements.html', context=context)


def get_client_ip(request):
    ip = request.META.get('REMOTE ADDR')
    return ip


class About(TemplateView):
    template_name = 'advertisements/about.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Бесплатные объявления в вашем городе"
        context['title'] = "Описание сайта"
        context['description'] = """
                      Универсальный сайт для размещения бесплатных объявлений в любой категории товаров и услуг. 
                      Можно размещать неограниченное количество объявлений бесплатно. 
                      Доски бесплатных объявлений в России на сайте. 
                      Популярная барахолка, частные объявления в России без регистрации. 
                      Разместить своё объявление бесплатно, быстро, купить, продать без посредников у частных лиц"""
        return context


class AdvertisementListView(generic.ListView):
    model = Advertisement
    template_name = 'advertisements_list.html'
    context_object_name = 'advertisement_list'
    queryset = Advertisement.objects.all()


class AdvertisementDetailView(generic.DetailView):
    model = Advertisement

    def get_object(self):
        obj = super().get_object()
        obj.views_count += 1
        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        obj.price_USD = round(obj.price_RUB / float(data['Valute']['USD']['Value']), 2)
        obj.save()
        return obj







