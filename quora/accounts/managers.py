from django.db import models
from django.contrib.auth.models import BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, username, password=None):
        if not email:
            raise ValueError('users must have an email address')
        user=self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, date_of_birth, username, password=None):
        user=self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            username=username,
        )
        user.is_admin=True
        user.save(using=self._db)

        return user

    #query_set for users must me added
