from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    # username = forms.CharField(label='Логин', widget=forms.TextInput)
    first_name = forms.CharField(max_length=30, label='Имя', required=True, widget=forms.TextInput)
    last_name = forms.CharField(max_length=30, label='Фамилия', required=False, widget=forms.TextInput)
    city = forms.CharField(max_length=30, label='Город', required=False, widget=forms.TextInput)
    date_of_birth = forms.DateField(label='Дата рождения', required=False, widget=forms.DateInput)
    number_phone = forms.CharField(label='Номер телефона', required=False, widget=forms.TextInput)
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'city', 'number_phone',
                  'date_of_birth', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

