from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import RegistrationForm


def login_view(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    return render(request, template_name='accounts/login.html', context={'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'accounts/logout.html', {})


def user_registration(request):
    user_register_form = RegistrationForm()
    if request.method == 'POST':
        user_register_form: RegistrationForm = RegistrationForm(request.POST, files=request.FILES)
        if user_register_form.is_valid():
            accounts: user_register_form.save(commit=False)
            accounts.save()
            return redirect('users:login')

    return render(
        request,
        template_name='user/registration.html',
        context={
            'form': user_register_form,
        }
    )


def register_view(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login')
    context = {"form": form}
    return render(request, "accounts/register.html", context)
