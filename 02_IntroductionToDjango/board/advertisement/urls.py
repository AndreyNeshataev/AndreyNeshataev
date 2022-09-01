from django.urls import path
from . import views

urlpatterns = [
    path("", views.advertisement_list, name='advertisement_list'),
    path('python_basic.html', views.python_basic, name='python_basic'),
    path('django.html', views.django, name='django'),
    path('python_advanced.html', views.python_advanced, name='python_advanced'),
    path('sql.html', views.sql, name='sql'),
    path('web.html', views.web, name='web')
]


