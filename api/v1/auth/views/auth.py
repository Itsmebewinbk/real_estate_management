from api.v1.auth.serializers import AuthSerializer, UserSerializer
from rest_framework.generics import CreateAPIView, GenericAPIView
from moonhive_real_estate.response import SuccessResponse, ErrorResponse
from django.conf import settings
import jwt
from auth_user.models import ActiveToken
from moonhive_real_estate.permission import IsAuthenticatedUser, IsAdmin


class RegisterView(CreateAPIView):
    permission_classes = (IsAuthenticatedUser, IsAdmin)
    serializer_class = UserSerializer
    serializer_classes = UserSerializer


class LoginView(CreateAPIView):
    serializer_class = AuthSerializer

    def post(self, request, *args, **kwargs):
        token_serializer = AuthSerializer(data=request.data)

        if token_serializer.is_valid():
            return SuccessResponse(
                data=token_serializer.validated_data,
                message="Login successful",
            )

        message = "Error"
        if token_serializer.errors.get("non_field_errors"):
            message = token_serializer.errors["non_field_errors"][0]

        return ErrorResponse(message=message)


class LogoutView(GenericAPIView):
    permission_classes = (IsAuthenticatedUser,)

    def post(self, request):
        token = request.META.get("HTTP_AUTHORIZATION").split()[1]
        jwt_secret = settings.SIMPLE_JWT.get("SIGNING_KEY")
        jti = jwt.decode(token, jwt_secret, algorithms=["HS256"])["jti"]
        ActiveToken.objects.filter(jti=jti).delete()
        return SuccessResponse(message="Successfully logged out")
