from django.shortcuts import render
from django.conf import settings


def index(request):
    return render(
        request,
        str(settings.BASE_DIR) + "/moonhive_real_estate/templates/index.html"
    )

