from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser


class CustomUserManager(BaseUserManager):
    def create_user(self, name, username, password, email=None,
                    is_active=True):
        if not name:
            raise ValueError("User must have name")
        if not username:
            raise ValueError("User must have username")
        user_obj = self.model(
            name=name,
            username=username,
            email=email,
        )
        user_obj.set_password(password)
        user_obj.active = is_active

        user_obj.save(using=self.db)
        return user_obj


class CustomUser(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=255, blank=False, unique=True)
    active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_active(self):
        return self.active
