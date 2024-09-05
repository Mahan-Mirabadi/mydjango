from django import forms
from django.contrib.auth.models import User
class UserRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'user_name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'email@gmail.com'}))
    first_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'first_name'}))
    last_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'last_name'}))
    password_1 = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    password_2 = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'placeholder':'repeat your password'}))
    
    def clean_user_name(self):
        user = self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('Username already exists')
        else:return user
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('email already exists')
        else:return email
    def clean_password_2(self):
        pass1=self.cleaned_data['password_1']
        pass2=self.cleaned_data['password_2']
        if pass1!=pass2:
            raise forms.ValidationError('password 1 and 2 are not the same')
        elif len(pass2)<8:
            raise forms.ValidationError('password is shorter than 8 characters')
        elif not any(char.isdigit() for char in pass2) or not any(char.isalpha() for char in pass2):
            raise forms.ValidationError('Password must contain letters and numbers')
        elif not any(i.isupper() for i in pass2):
            raise forms.ValidationError('Password must contain uppercase letter')
        else:return pass1
class UserLoginForm(forms.Form):
    user=forms.CharField(max_length=30)
    password=forms.CharField(max_length=50)
class ChangePasswordForm(forms.Form):
    old_pass=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'old_password'}))
    new_pass=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'new_password'}))
    new_pass2=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'new_password'}))