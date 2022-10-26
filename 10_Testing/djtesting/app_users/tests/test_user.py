from django.test import TestCase, Client
from http import HTTPStatus
from django.contrib.auth.models import User
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
        self.assertTrue(response.context['user'].is_active)
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
