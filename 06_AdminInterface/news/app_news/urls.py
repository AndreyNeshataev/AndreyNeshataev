from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsHome.as_view(), name='news'),
    path('about/', About.as_view(), name='about'),
    path('news_add/', AddNews.as_view(), name='news_add'),
    # path('news/<slug:news_slug>/', ViewingArticle.as_view(), name='news'),
    path('news/<int:pk>', ViewingArticle.as_view(), name='news_detail'),
    path('news/<int:pk>/update', UpdateNews.as_view(), name='news_update'),

]
