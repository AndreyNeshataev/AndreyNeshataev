from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from app_users.models import Profile

from .forms import *


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        city = form.cleaned_data.get('city')
        date_of_birth = form.cleaned_data.get('date_of_birth')
        number_phone = form.cleaned_data.get('number_phone')
        about_me = form.cleaned_data.get('about_me')
        Profile.objects.create(
            user=user,
            city=city,
            date_of_birth=date_of_birth,
            number_phone=number_phone,
            about_me=about_me
        )
        login(self.request, user)
        return redirect('blog_list')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'


class LogoutUser(LogoutView):
    pass


class MyUser(ListView):
    model = User
    template_name = 'users/account.html'


class ChangeUser(UpdateView):
    form_class = ChangeUserForm
    template_name = 'users/change_user.html'
    queryset = User.objects
    success_url = reverse_lazy('account_url')

    def post(self, request, *args, **kwargs):
        obj = self.get_form()
        avatars = request.FILES.getlist('avatar')
        for avatar in avatars:
            print(avatar)
        if obj.is_valid():
            new_info = User.objects.get(id=request.user.id)
            new_info.firs_name = obj.cleaned_data.get('firs_name')
            new_info.last_name = obj.cleaned_data.get('last_name')
            new_info.save()
            new_profile = Profile.objects.get(user_id=request.user.id)
            new_profile.about_me = obj.cleaned_data['about_me']
            for avatar in avatars:
                new_profile.avatar = avatar
            new_profile.save()
            return redirect('account_url')
        return render(request, 'users/change_user.html', {'form': obj})