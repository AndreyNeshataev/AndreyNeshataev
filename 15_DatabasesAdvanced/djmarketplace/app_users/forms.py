from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from app_users.models import Profile
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label=_('Логин'))
    first_name = forms.CharField(max_length=30, label=_('Имя'), required=True)
    last_name = forms.CharField(max_length=30, label=_('Фамилия'), required=False)
    city = forms.CharField(max_length=30, label=_('Город'), required=False)
    date_of_birth = forms.DateField(label=_('Дата рождения'), required=False)
    number_phone = forms.CharField(label=_('Номер телефона'), required=False)
    password1 = forms.CharField(label=_('Пароль'))
    password2 = forms.CharField(label=_('Повтор пароля'))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'city', 'date_of_birth',
                  'number_phone', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'number_phone': forms.TextInput(attrs={'class': 'form-control'}),
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
    password = None
    city = forms.CharField(max_length=50, label=_('Город'), required=False)
    number_phone = forms.CharField(label=_('Номер телефона'), required=False)

    class Meta:
        model = Profile
        fields = ('city', 'number_phone')

        widgets = {
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'number_phone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ReplenishmentBalanceForm(forms.ModelForm):
    amount_balance = forms.FloatField(label=_('Сумма пополнения'), required=True)

    class Meta:
        model = Profile
        fields = ('amount_balance',)

        widgets = {
            'amount_balance': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_amount_balance(self):
        amount_balance = self.cleaned_data['amount_balance']
        if amount_balance <= 0:
            raise ValidationError(_("На эту сумму невозможно пополнить баланс"))
        return amount_balance
