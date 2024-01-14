from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager


class Manager(UserManager):
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields["is_superuser"] = True
        super(Manager, self).create_superuser(username, email, password, **extra_fields)


class User(AbstractUser):
    name = models.CharField(max_length=200)

    objects = Manager()

    def __str__(self):
        return self.username


class ActiveToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jti = models.CharField(max_length=200, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
