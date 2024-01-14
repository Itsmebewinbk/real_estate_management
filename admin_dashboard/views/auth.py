from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from admin_dashboard.forms import LogInForm
from admin_dashboard.decorators import admin_login


def login_view(request, *args, **kwargs):
    form = LogInForm()
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user and user.is_superuser:
                login(request, user)
                messages.success(request, "Login Succesfull")
                return redirect("property_list")
            else:
                messages.error(request, "invalid username or password")
    return render(request, "login.html", {"form": form})


@admin_login
def logout_view(request):
    logout(
        request,
    )
    return redirect("login")
