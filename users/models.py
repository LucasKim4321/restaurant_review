from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password, *args, **kwargs):
        if not email:
            raise ValueError('must have user email')
        user = self.model(email=self.normalize_email(email), *args, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, *args, **kwargs):
        user = self.create_user(email=self.normalize_email(email), password=password, *args, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(PermissionsMixin, AbstractBaseUser):
    nickname = models.CharField('닉네임', max_length=20, unique=True)
    email = models.EmailField('이메일', max_length=40, unique=True)
    profile_image  = models.ImageField('프로필 이미지', upload_to='users/profile_images', default='users/blank_profile_image.png')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
