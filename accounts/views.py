from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, EditProfilePageForm, ChangePasswordPageForm
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from .models import Account
from django.views.generic import DeleteView
from django.utils.translation import gettext_lazy as _


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is None:
            context = { "error": _("You have either entered the wrong credentials or you are not a registered user, please either login or register")}
            return render(request, "accounts/login.html",context)
        login(request, user)
        return redirect("/")
    return render(request, "accounts/login.html", {})

def logout_view(request):
    logout(request)
    return redirect("/account/login")

def register_view(request):
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect("/")
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, "accounts/register.html", context) 

def user_profile_page_view(request):
    context = {'user': request.user}
    return render(request, "accounts/profile.html", context) 

def user_edit_profile_page_view(request):
    context = {}
    if request.method == 'POST':
        form = EditProfilePageForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("/account/profile")
        else:
           context['edit_profile_form'] = form
    else:
        form = EditProfilePageForm(instance=request.user)
        context['edit_profile_form'] = form
    return render(request, "accounts/profile_edit.html", context)

def user_change_password_view(request):
    context = {}
    if request.method == 'POST':
        form = ChangePasswordPageForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("/account/profile")
        else:
           context['change_password_form'] = form
    else:
        form = ChangePasswordPageForm(user=request.user)
        context['change_password_form'] = form
    return render(request, "accounts/change_password.html", context)

class UserDeleteView(DeleteView):
    model = Account
    success_url = reverse_lazy('home')

