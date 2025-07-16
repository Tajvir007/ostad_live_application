from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError(_('Please enter an email address'))

        email=self.normalize_email(email)

        new_user=self.model(email=email,**extra_fields)

        new_user.set_password(password)

        new_user.save()

        return new_user


    def create_superuser(self,email,password,**extra_fields):

        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))


        return self.create_user(email,password,**extra_fields)


class User(AbstractUser):
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    password = models.CharField(max_length=100)
    otp = models.CharField(max_length=50,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    password_forget_token = models.CharField(max_length=300,null=True,blank=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    objects = CustomUserManager()


class Club(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modifyed_at = models.DateTimeField(auto_now=True)
    created_by = models.EmailField(null=True,blank=True)




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    club = models.ManyToManyField(Club)
    phone = models.CharField(max_length=20, null=True, blank=False)
    sponsor_email = models.EmailField()

    def __str__(self) -> str:
        return self.user.email