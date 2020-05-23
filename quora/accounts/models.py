from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import MyUserManager

class MyUser(AbstractBaseUser):
    username=models.CharField(max_length=50)
    email=models.EmailField(
        verbose_name='email_address',
        max_length=250,
        unique=True,
    )
    date_of_birth=models.DateField()
    profile_image=models.ImageField(upload_to='profile_pics/', blank=True)
    about=models.TextField()

    following=models.ManyToManyField('self', through=Contact,
                                    related_name='followers',
                                    symmetrical=False)

    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)

    objects=MyUserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['date_of_birth', 'username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        #Does the user have a specific permission ?
        return True

    def has_module_perms(self, app_label):
        #Does the user have permissions to view the app 'app_label'
        return True

    @property
    def is_staff(self):
        #is the user member of staff (admin)
        return self.is_admin
