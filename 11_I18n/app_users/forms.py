from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile
from django.utils.translation import gettext_lazy as _


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label=_('Логин'))
    first_name = forms.CharField(max_length=30, label=_('Имя'), required=True)
    last_name = forms.CharField(max_length=30, label=_('Фамилия'), required=False)
    city = forms.CharField(max_length=30, label=_('Город'), required=False)
    date_of_birth = forms.DateField(label=_('Дата рождения'), required=False)
    number_phone = forms.CharField(label=_('Номер телефона'), required=False)
    email = forms.EmailField(label='Email', required=False)
    about_me = forms.CharField(label=_('Обо мне'), required=False)
    avatar = forms.FileField(label=_('Добавить Аватар'), required=False)
    password1 = forms.CharField(label=_('Пароль'))
    password2 = forms.CharField(label=_('Повтор пароля'))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'city', 'date_of_birth',
                  'number_phone', 'email', 'about_me', 'avatar', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'number_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'about_me': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'avatar': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label=_('Логин'))
    password = forms.CharField(label=_('Пароль'))

    class Meta:
        model = User
        fields = ('username', 'password')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class ChangeUserForm(UserChangeForm):
    password = None
    first_name = forms.CharField(max_length=30, label=_('Имя'), required=True)
    last_name = forms.CharField(max_length=30, label=_('Фамилия'), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ChangeProfileForm(UserChangeForm):
    about_me = forms.CharField(max_length=500, label=_('Обо мне'), required=False)
    avatar = forms.FileField(label=_('Изменить Аватар'), required=False)
    password = None

    class Meta:
        model = Profile
        fields = ('avatar', 'about_me')

        widgets = {
            'about_me': forms.Textarea(attrs={'class': 'form-control'}),
            'avatar': forms.TextInput(attrs={'class': 'form-control'}),
        }


class RestorePasswordForm(forms.Form):
    email = forms.EmailField()