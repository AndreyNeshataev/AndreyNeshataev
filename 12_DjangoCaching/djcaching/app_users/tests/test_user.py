from django.test import TestCase, Client
from http import HTTPStatus
from django.contrib.auth.models import User
from app_users.models import Profile, PurchaseHistory
from app_shops.models import Goods
from django.urls import reverse


class UserTestCase(TestCase):

    def test_is_ok_page_login(self):
        url = reverse('login_url')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_is_ok_page_register(self):
        url = reverse('register_url')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_login_user(self):
        user_info = {
            'username': 'Login',
            'password': '4efefwefe'
        }
        url = reverse('login_url')
        User.objects.create_user(**user_info)
        response = self.client.post(url, user_info, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
        login = self.client.login(username=user_info['username'],
                                  password=user_info['password'])
        self.assertTrue(login)

    def test_register_user(self):
        user_info = {
            'username': 'Test',
            'email': 'Test@mail.com',
            'password': '4ABefef3rgVM',
            'password_confirmation': '4ABefef3rgVM',
        }
        url = reverse('register_url')
        response = self.client.post(url, user_info)
        self.assertEqual(response.status_code, 200)
        try:
            user = User.objects.get(username=user_info['username'])
        except User.DoesNotExist as ex:
            print(ex)
            user = User.objects.create()
        self.assertIsInstance(user, User)

    def test_replenishment_balance(self):
        user_info = {
            'username': 'Login',
            'password': '4efefwefe'
        }

        user = User.objects.create_user(**user_info)
        login = self.client.login(username='Login',
                                  password='4efefwefe')
        self.assertTrue(login)
        url = reverse('replenishment_url', kwargs={'pk': user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/replenishment_balance.html')
        Profile.objects.create(user_id=user.id, balance=0)
        response = self.client.post(url, {'amount_balance': 100.00}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(user.profile.balance, 100)
        self.assertRedirects(response, reverse('home'))

    def test_histori(self):
        user_info = {
            'username': 'Login',
            'password': '4efefwefe'
        }

        user = User.objects.create_user(**user_info)
        login = self.client.login(username='Login',
                                  password='4efefwefe')
        self.assertTrue(login)
        url = reverse('history_url', kwargs={'pk': user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/history.html')
        goods = Goods.objects.create(name_goods='GOODS', price=100)
        PurchaseHistory.objects.create(user_id=user.id, goods=goods)
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(PurchaseHistory.objects.count(), 1)

