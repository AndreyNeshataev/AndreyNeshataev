from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from app_users.models import Profile
from django.http import HttpResponse
from django.core.mail import send_mail

from .forms import *


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        avatars = request.FILES.getlist('avatar')
        if form.is_valid():
            user = form.save()
            city = form.cleaned_data.get('city')
            date_of_birth = form.cleaned_data.get('date_of_birth')
            number_phone = form.cleaned_data.get('number_phone')
            about_me = form.cleaned_data.get('about_me')
            profile = Profile.objects.create(user=user,
                                             city=city,
                                             date_of_birth=date_of_birth,
                                             number_phone=number_phone,
                                             about_me=about_me
                                             )
            if avatars:
                for avatar in avatars:
                    profile.avatar = avatar
            profile.save()
            login(self.request, user)
            return redirect('account_url')
        return render(request, 'users/register.html', {'form': form})


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'


class LogoutUser(LogoutView):
    pass


class MyUser(ListView):
    model = User
    template_name = 'users/account.html'


class ChangeUser(UpdateView):
    success_url = reverse_lazy('account_url')

    def get(self, request, *args, **kwargs):
        my_profile = Profile.objects.get(user_id=self.request.user.id)
        my_user = User.objects.get(id=self.request.user.id)
        profile_form = ChangeProfileForm(instance=my_profile)
        user_form = ChangeUserForm(instance=my_user)
        return render(request, 'users/change_user.html', {'profile_form': profile_form,
                                                          'user_form': user_form})

    def post(self, request, *args, **kwargs):
        avatars = request.FILES.getlist('avatar')
        my_profile = Profile.objects.get(user_id=self.request.user.id)
        my_user = User.objects.get(id=self.request.user.id)
        profile_form = ChangeProfileForm(request.POST, instance=my_profile)
        user_form = ChangeUserForm(request.POST, instance=my_user)
        if user_form.is_valid() and profile_form.is_valid():
            my_user.first_name = user_form.cleaned_data.get('first_name')
            my_user.last_name = user_form.cleaned_data.get('last_name')
            my_user.save()
            my_profile.about_me = profile_form.cleaned_data['about_me']
            if avatars:
                for avatar in avatars:
                    my_profile.avatar = avatar
            my_profile.save()
            return redirect('account_url')
        return render(request, 'users/change_user.html', {'profile_form': profile_form,
                                                          'user_form': user_form})


def restore_password(request):
    if request.method == 'POST':
        form = RestorePasswordForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            new_password = User.objects.make_random_password()
            current_user = User.objects.filter(email=user_email).first()
            if current_user:
                current_user.set_password(new_password)
                current_user.save()
            send_mail(subject='Восстановление пароля',
                      message='Test',
                      from_email='admin@company.com',
                      recipient_list=[form.cleaned_data['email']]
                      )
            return HttpResponse('Письмо с новым паролем было успешно оправлено')
    restore_password_form = RestorePasswordForm()
    context = {'form': restore_password_form}
    return render(request, 'users/restore_password.html', context=context)











