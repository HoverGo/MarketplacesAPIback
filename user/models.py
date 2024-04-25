from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    def create_user(self, name, email, phone, password):
        if name is None:
            raise TypeError("User must have a name")

        if email is None:
            raise TypeError("User must have a email")

        if phone is None:
            raise TypeError("User must have a phone number")

        if password is None:
            raise TypeError("User must have a password")

        user = self.model(name=name, email=self.normalize_email(email), phone=phone)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, name, email, phone, password):
        user = self.create_user(name, email, phone, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r"^[а-яА-ЯёЁa-zA-Z]+\s[а-яА-ЯёЁa-zA-Z]+\s[а-яА-ЯёЁa-zA-Z]+$",
                message=("Invalid full name"),
                code="invalid_full_name",
            )
        ],
    )
    password = models.CharField(
        max_length=250,
        validators=[
            RegexValidator(
                regex=r"^[A-Za-z\d!@#$%^&*()_+]+$",
                message=("Invalid password"),
                code="invalid_password",
            ),
        ],
    )
    email = models.EmailField(unique=True, max_length=100)
    phone = models.CharField(
        validators=[RegexValidator(regex=r"^1?\d{9,15}$")],
        max_length=20,
        unique=True,
    )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["name", "email"]

    objects = UserManager()

    def __str__(self):
        return self.email
