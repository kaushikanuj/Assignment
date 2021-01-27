from django.shortcuts import render, HttpResponseRedirect
from .forms import SingUpForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
# SignUp
def sign_up(request):
    if request.method == "POST":
        fm = SingUpForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = SingUpForm()
    return render(request, 'core/signup.html', {'form': fm})


# Login View
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
    else:
        return HttpResponseRedirect('/profile/')
    return render(request, 'core/userlogin.html', {'form': fm})


# Profile
def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'core/profile.html', {'username': request.user})
    else:
        return HttpResponseRedirect('/userlogin/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/userlogin/')


def change_password(request):
    if request.method == 'POST':
        fm = PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/profile/')
    else:
        fm = PasswordChangeForm(user=request.user)
    return render(request, 'core/changepassword.html', {'form': fm})
