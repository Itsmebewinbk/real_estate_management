from rest_framework import serializers
from auth_user.models import User, ActiveToken
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


def get_token(user):
    token = TokenObtainPairSerializer.get_token(user)
    access, refresh = token.access_token, token
    ActiveToken.objects.create(user=user, jti=access["jti"])
    return access, refresh


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        write_only=True,
        required=False,
    )

    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "username",
            "password",
        )

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.is_staff = True
        user.is_superuser = True
        user.set_password(validated_data["password"])
        user.save(update_fields=["password", "is_staff", "is_superuser"])
        return user


class AuthSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=128,
        write_only=True,
        required=False,
    )
    password = serializers.CharField(
        max_length=128,
        write_only=True,
        required=False,
    )

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        if username and password:
            user = authenticate(
                username=username,
                password=password,
            )

            if not user:
                raise serializers.ValidationError("Invalid Credentials")

            access, refresh = get_token(user)

            user_serializer = UserSerializer(user)
            data = {
                "token": {"access": str(access), "refresh": str(refresh)},
                "user": user_serializer.data,
            }
            return data
        else:
            raise serializers.ValidationError("Must include username and password")
