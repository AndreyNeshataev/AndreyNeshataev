from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView


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
        return News.objects.filter(activity_flag=True)


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


class ViewingArticle(DetailView, CreateView):
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
        print(form)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.news = self.get_object()
        self.object.save()
        return super().form_valid(form)



