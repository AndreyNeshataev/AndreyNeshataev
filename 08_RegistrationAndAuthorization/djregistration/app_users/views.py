from datetime import datetime
from django.shortcuts import render, redirect
from .forms import LoginUserForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from app_users.models import Profile

from .forms import *


# Create your views here.


# def login_view(request):
#     if request.method == 'POST':  # Для POST пытаемся аутентифицировать пользователя
#         auth_form = AuthForm(request.POST)
#         if auth_form.is_valid():
#             username = auth_form.cleaned_data['username']
#             password = auth_form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user:
#                 if user.is_active:
#                     if not user.is_superuser:
#                         now = datetime.now()
#                         hour_now = now.hour
#                         if 7 < hour_now < 22:
#                             login(request, user)
#                             return HttpResponse('Вы успешно вошли в систему')
#                         else:
#                             auth_form.add_error('__all__', 'Ошибка! В ночное время вход запрещен!')
#                     else:
#                         auth_form.add_error('__all__', 'Ошибка! Администраторам вход запрещен!')
#                 else:
#                     auth_form.add_error('__all__', 'Ошибка! Учетная запись пользователя не активна!')
#             else:
#                 auth_form.add_error('__all__', 'Ошибка! Проверьте правильность ввода логина и пароля!')
#     else:  # для всех остальных запросов просто отображаем саму страницу логина
#         auth_form = AuthForm()
#
#     context = {
#         'form': auth_form
#     }
#     return render(request, 'users/login.html', context=context)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        city = form.cleaned_data.get('city')
        date_of_birth = form.cleaned_data.get('date_of_birth')
        number_phone = form.cleaned_data.get('number_phone')
        Profile.objects.create(
            user=user,
            city=city,
            date_of_birth=date_of_birth,
            number_phone=number_phone
        )
        login(self.request, user)
        return redirect('news')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'


class LogoutUser(LogoutView):
    template_name = 'users/logout.html'


class MyUser(ListView):
    model = User
    template_name = 'users/account.html'
