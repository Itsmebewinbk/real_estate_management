from django.urls import path, include


urlpatterns = [
    path("auth/", include("api.v1.auth.urls")),
    path("common/", include("api.v1.common.urls")),
    path("core/", include("api.v1.core.urls")),
]
