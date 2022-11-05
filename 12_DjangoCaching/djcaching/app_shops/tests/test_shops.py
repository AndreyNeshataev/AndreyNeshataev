import datetime
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from app_users.models import Profile
from app_shops.models import Shop, Goods, Offers


class ShopTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='4efefwefe'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            balance=500
        )
        self.shop = Shop.objects.create(
            name_shop='A good shop',
            sale_date=datetime.date.today()
        )
        self.goods = Goods.objects.create(
            shop=self.shop,
            name_goods='A good goods',
            price=100,
            sale=10
        )

    def test_string_representation(self):
        shop = Shop(name_shop='A new shop')
        self.assertEqual(str(shop), shop.name_shop)

    def test_shop(self):
        self.assertEqual(f'{self.shop.name_shop}', 'A good shop')
        self.assertEqual(f'{self.shop.sale_date}', str(datetime.date.today()))

    def test_goods(self):
        self.assertEqual(f'{self.goods.shop}', self.shop.name_shop)
        self.assertEqual(f'{self.goods.name_goods}', 'A good goods')
        self.assertEqual(f'{self.goods.price}', '100')
        self.assertEqual(f'{self.goods.sale}', '10')

    def test_home(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shops/home.html')

    def test_shop_list(self):
        url = reverse('shops_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shops/shops_list.html')

    def test_shop_page(self):
        url = reverse('shop_page', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shops/shop_page.html')

    def test_shop_page_unauthenticated(self):
        url = reverse('shop_page', kwargs={'pk': self.user.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)

    def test_shop_page_authenticated(self):
        goods = {
            'shop': self.shop,
            'name_goods': 'A good goods',
            'price': 100,
            'sale': 10
        }
        login = self.client.login(username='testuser',
                                  password='4efefwefe')
        self.assertTrue(login)
        url = reverse('shop_page', kwargs={'pk': self.user.pk})
        response = self.client.post(url, goods, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('home'))



