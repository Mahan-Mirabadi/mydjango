from django.shortcuts import render, redirect
from . forms import UserRegisterForm,UserLoginForm,ChangePasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.
def ViewContactUs(request):
    if request.method=='POST':
        form_register = UserRegisterForm(request.POST)
        if form_register .is_valid():
            data = form_register.cleaned_data
            User.objects.create_user(username=data['user_name'], email=data['email'], password=data['password_2'])
            return redirect('products:ViewThanks')
    else:
        form_register=UserRegisterForm
    context={'form_register':form_register} 
    return render(request,'contactus/contactpage.html', context=context)
def ViewLogin(request):
    if request.method=='POST':
        form_login = UserLoginForm(request.POST)
        if form_login.is_valid():
            data = form_login.cleaned_data
            try:
                user = authenticate(request, username=User.objects.get(email=data['user']), password=data['password'])
            except:
                user=authenticate(request,username=data['user'],password=data['password'])
            if user is not None:
                login(request,user)
                return redirect('products:ViewHome')
    else:
        form_login = UserLoginForm()
    context = {'form_login':form_login}
    return render(request,'contactus/login.html')
def Logout(request):
    pass
def ViewchangePassword(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        user=request.user
        if form.is_valid():
            data=form.cleaned_data
            old_password=data['old_password']
            new_password=data['new_password']
            new_password2=data['new_password2']
            if not user.check_password(old_password):
                return HttpResponse ("wrong password")
            elif new_password != new_password2:
                return HttpResponse ("passwords are not matched")
            else:
                user.set_password(new_password2)
                login(request.user)
                user.save()
                return redirect ('home:view-home')
    else:
        form=ChangePasswordForm()
    return render(request,'contactus/changepassword.html', context={'form':form})

