from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин')
    first_name = forms.CharField(max_length=30, label='Имя', required=True)
    last_name = forms.CharField(max_length=30, label='Фамилия', required=False)
    city = forms.CharField(max_length=30, label='Город', required=False)
    date_of_birth = forms.DateField(label='Дата рождения', required=False)
    number_phone = forms.CharField(label='Номер телефона', required=False)
    email = forms.EmailField(label='Email', required=False)
    about_me = forms.CharField(label='Обо мне', required=False)
    avatar = forms.FileField(label='Добавить Аватар', required=False)
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Повтор пароля')

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
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль')

    class Meta:
        model = User
        fields = ('username', 'password')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class ChangeUserForm(UserChangeForm):
    password = None
    first_name = forms.CharField(max_length=30, label='Имя', required=True)
    last_name = forms.CharField(max_length=30, label='Фамилия', required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ChangeProfileForm(UserChangeForm):
    about_me = forms.CharField(max_length=500, label='Обо мне', required=False)
    avatar = forms.FileField(label='Изменить Аватар', required=False)
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