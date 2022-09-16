from django.urls import path
from . import views
from .views import About, AdvertisementListView, AdvertisementDetailView

urlpatterns = [
    path('', views.advertisement_list, name='advertisement'),
    path('', views.get_client_ip, name='user_ip'),
    path('about/', About.as_view(), name='about'),
    path('advertisements/', AdvertisementListView.as_view(), name='advertisement'),
    path('advertisements/<int:pk>', AdvertisementDetailView.as_view(), name='advertisement-detail')
]
