from django.urls import path
from app_shops.views import home_page, shops_list, ShopPage  # , shop_page

urlpatterns = [
    path('', home_page, name='home'),
    path('shops_list', shops_list, name='shops_list'),
    path('<int:pk>/shop_page', ShopPage.as_view(), name='shop_page'),
]
