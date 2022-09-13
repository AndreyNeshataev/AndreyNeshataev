from django.urls import path
from . import views

urlpatterns = [
    path('', views.Advertisements.as_view()),
    path('advertisements/', views.ListAdvertisements.as_view()),
    path('contacts/', views.Contacts.as_view()),
    path('about/', views.About.as_view()),
    path('categories/', views.Categories.as_view()),
    path('regions/', views.Regions.as_view())
]
