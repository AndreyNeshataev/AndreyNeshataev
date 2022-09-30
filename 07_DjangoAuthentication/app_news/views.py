from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
from django.views.generic.edit import FormMixin
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
        context['menu'] = menu
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.all()


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


class AddNews(CreateView):
    form_class = NewsForm
    template_name = 'app_news/news_add.html'
    success_url = reverse_lazy('news')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        return context


class UpdateNews(UpdateView):
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
    # slug_url_kwarg = 'news_slug'
    context_object_name = 'news'
    form_class = CommentsForm
    success_msg = 'Комментарий успешно создан'
    success_url = reverse_lazy('news')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comments.objects.filter(news_id=self.get_object().id)
        context['commentary'] = comments
        context['title_commentary'] = 'КОММЕНТАРИИ:'
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        # if not request.user.is_authenticated:
        #     User.objects.create(username=request.POST.get('user_name'))
        # form = CommentsForm(request.POST)
        # print(form['commentary'], form['user_name'])
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
            self.object.author = self.request.POST.get('user_name')
        self.object.save()
        return super().form_valid(form)
