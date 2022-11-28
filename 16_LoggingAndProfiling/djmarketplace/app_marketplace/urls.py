from django.urls import path
from app_marketplace.views import shops_list, ShopPage, HomePage, report_on_best_selling

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('shops_list', shops_list, name='shops_list'),
    path('<int:pk>/shop_page', ShopPage.as_view(), name='shop_page'),
    path('<int:pk>/shop_page/<int:pk_2>', ShopPage.as_view(), name='shop_page'),
    path('report/<int:pk>', report_on_best_selling, name='report'),
]
