from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, **extra_fields)


class Employer(AbstractBaseUser, PermissionsMixin):

    POSITION_CHOICES = (
        ("HR", "HR"),
        ("Manager", "Manager"),
        ("TeamLead", "Team Lead"),
        ("Backend Developer", "Backend Developer"),
        ("Frontend Developer", "Frontend Developer"),
        ("Designer", "Designer"),
        ("Tester", "Tester"),
    )

    RANK_STATUS = (
        ("Junior", "Junior"),
        ("Senior", "Senior"),
        ("Expert", "Expert"),
    )

    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    email      = models.EmailField(unique=True)
    position   = models.CharField(max_length=255, choices=POSITION_CHOICES)
    rank       = models.CharField(max_length=255, choices=RANK_STATUS, default="Junior")
    is_active  = models.BooleanField(default=True)
    is_staff   = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD  = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "position", "rank"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
