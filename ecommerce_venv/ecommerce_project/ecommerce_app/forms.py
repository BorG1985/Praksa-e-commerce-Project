from logging import PlaceHolder
from django import forms
from django.contrib.auth.models import User
from .models import NewUser
from django.forms import ModelForm


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"placeholder": "Enter e-mail to login", 'style': 'width: 300px; height: 30px; border:2px solid aqua;border-radius: 8px;margin-bottom:10px;'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Enter password to login", 'style': 'width: 300px; height: 30px; border:2px solid aqua;border-radius: 8px;margin-bottom:10px;'}), label='')


class UserRegistrationForm(ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                             "placeholder": "Enter e-mail to login", 'style': 'width: 300px; height: 30px; border:2px solid aqua; border-radius: 8px;margin-bottom:10px;'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Enter password to register", 'style': 'width: 300px; height: 30px; border:2px solid aqua;border-radius: 8px;margin-bottom:10px;'}), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Repeat password to register", 'style': 'width: 300px; height: 30px; border:2px solid aqua;border-radius: 8px;margin-bottom:10px;'}), label='')
    name = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Enter your name", 'style': 'width: 300px; height: 30px; border:2px solid aqua; border-radius: 8px;margin-bottom:10px;'}), label='')
    surname = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Enter your surename", 'style': 'width: 300px; height: 30px; border:2px solid aqua; border-radius: 8px;margin-bottom:10px;'}), label='')
    address = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Enter your address", 'style': 'width: 300px; height: 30px; border:2px solid aqua; border-radius: 8px;margin-bottom:10px;'}), label='')
    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Enter your phone number", 'style': 'width: 300px; height: 30px; border:2px solid aqua; border-radius: 8px;margin-bottom:10px;'}), label='')

    class Meta:
        model = NewUser
        fields = ('email', 'password', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
