from rest_framework.permissions import IsAuthenticated, BasePermission
from django.conf import settings
import jwt
from auth_user.models import ActiveToken


class IsAuthenticatedUser(IsAuthenticated):
    def has_permission(self, request, view):
        if not request.user.is_anonymous and super(
            IsAuthenticatedUser, self
        ).has_permission(request, view):
            jwt_secret = settings.SIMPLE_JWT.get("SIGNING_KEY")
            token = request.META.get("HTTP_AUTHORIZATION").split()[1]
            jti = jwt.decode(token, jwt_secret, algorithms=["HS256"])["jti"]
            if ActiveToken.objects.filter(jti=jti).exists():
                return True
        return False


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if (
            request.user.is_superuser
            and request.user.is_staff
            and super(IsAdmin, self).has_permission(request, view)
        ):
            return True
        return False
