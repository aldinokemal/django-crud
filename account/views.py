from django.contrib.auth import authenticate, login as sign_in, logout as sign_out
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm


# def authenticated(request):
#     if request.user.is_authenticated:
#         return True
#     else:
#         return False


# Create your views here.
def redirect_login(request):
    return redirect('/account/login/')

def login(request):
    if request.method == "POST":
        accountID = request.POST['accountID']
        password = request.POST['password']
        user = authenticate(account_id=accountID, password=password)
        # user = authenticate(username=accountID, password=password)
        if user is not None:
            # messages.success(request, 'Login Success')
            sign_in(request, user)
            return redirect('inventori:index')
        else:
            messages.error(request, 'Login Gagal')
            return redirect('account:login')
        # return redirect_login(request)]
    return render(request, "page_login.html", {'formRegister': RegisterForm()})


def logout(request):
    sign_out(request)
    return redirect('account:login')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            model.password = make_password(form.cleaned_data['password'])
            model.save()
            messages.success(request, 'Register Success.')
        else:
            return render(request, 'page_login.html', {'formRegister': form})

    return redirect("account:login")
