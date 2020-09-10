from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={
            'placeholder': "Введите свой логин",
            'id': "username",
            'class': 'input-xlarge',
    }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={
            'placeholder': "Введите ваш пароль",
            'id': "password",
            'class': "input-xlarge",

    }))


class UserRegistrationForm(forms.ModelForm):
    attributs = {
            'placeholder': "Пароль",
            'class': "input-xlarge"
    }
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs=attributs))
    password2 = forms.CharField(label='Повторите пароль',widget=forms.PasswordInput(
        attrs=attributs))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Ваши пароли не совпадают')
        return cd['password2']








