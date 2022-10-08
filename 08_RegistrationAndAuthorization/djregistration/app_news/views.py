from django.http import HttpResponse
from django.views.generic.edit import FormMixin
from django.contrib.auth.decorators import permission_required  # , login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView, TemplateView, CreateView, UpdateView
from datetime import timedelta, date

from .forms import *
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'news_add'},
        ]


class NewsHome(ListView):
    model = News
    template_name = 'app_news/news_list.html'
    context_object_name = 'news'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.username:
            if self.request.user.profile.verification_flag == 'Верифицирован':
                context['verifi'] = 'Ваша верификация подтверждена'
            else:
                context['no_verifi'] = 'Вы не прошли верификацию'
        context['menu'] = menu
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(published=True)


class About(TemplateView):
    template_name = 'app_news/about.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Новости"
        context['title'] = "Описание сайта"
        context['description'] = """
                      Сайт новостей с возможностью оставлять комментарии
                      """
        return context


class AddNews(PermissionRequiredMixin, CreateView):
    permission_required = 'app_news.add_news'
    form_class = NewsForm
    template_name = 'app_news/news_add.html'
    success_url = reverse_lazy('news')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        self.request.user.profile.number_published_news += 1
        self.request.user.profile.save()
        return context


class UpdateNews(PermissionRequiredMixin, UpdateView):
    permission_required = 'app_news.change_news'
    form_class = NewsForm
    template_name = 'app_news/news_update.html'
    success_url = reverse_lazy('news')

    def get_queryset(self):
        return News.objects

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменение статьи'
        return context


class ViewingArticle(UpdateView, DetailView):
    model = News
    template_name = 'app_news/news_detail.html'
    context_object_name = 'news'
    form_class = CommentsForm
    success_url = reverse_lazy('news')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comments.objects.filter(news_id=self.get_object().id)
        if self.request.user.profile.verification_flag == 'Верифицирован':
            context['verifi'] = True
        context['commentary'] = comments
        context['title_commentary'] = 'КОММЕНТАРИИ:'
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)  # HttpResponse('Не получилось')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.news = self.get_object()
        if self.request.user.is_authenticated:
            self.object.user_name = self.request.user
        else:
            self.object.author = self.request.POST.get('author')
        self.object.save()
        return super().form_valid(form)


class TagDetail(DetailView):
    model = Tag
    template_name = 'app_news/tag_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = Tag.objects.get(slug__iexact=self.get_object().slug)
        news = tag.news.filter(published=True)
        context['tag'] = tag
        context['news'] = news
        return context


def news_filter(request, pk):
    news = News.objects.filter(published=True)
    period = ''
    if pk == 1:
        news = news.filter(created_date__gte=date.today())
        period = 'Сегодня'
    elif pk == 2:
        week = date.today() - timedelta(minutes=60 * 24 * 7)
        news = news.filter(created_date__lt=date.today(), created_date__gte=week)
        period = 'Неделю'
    elif pk == 3:
        month = date.today() - timedelta(minutes=60 * 24 * 30)
        news = news.filter(created_date__lt=date.today(), created_date__gte=month)
        period = 'Месяц'
    return render(request, 'app_news/news_filter.html', context={'news': news,
                                                                 'title': 'Фильтр по дате',
                                                                 'header': 'Новости за {}'.format(period)})
