from django.shortcuts import redirect
from django.contrib import messages


def admin_login(fn):
    def wrapper(request, *args, **kwargs):
        if request.user.is_superuser and request.user.is_authenticated:
            return fn(request, *args, **kwargs)
        else:
            messages.error(request, "You must Login")
            return redirect("login")

    return wrapper
