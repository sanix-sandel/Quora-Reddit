from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Group
from django.contrib.auth import get_user_model
from .managers import MyUserManager
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import PermissionsMixin


class Contact(models.Model):
    user_from=models.ForeignKey(settings.AUTH_USER_MODEL,
                                related_name='rel_from_set',
                                on_delete=models.CASCADE)

    user_to=models.ForeignKey(settings.AUTH_USER_MODEL,
                                related_name='rel_to_set',
                                on_delete=models.CASCADE)

    created=models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering=('-created',)

    def __str__(self):
        return f"{self.user_from} follows {self.user_to}"


class Role(Group):
    class Meta:
        proxy=True
        verbose_name=("Role")
        verbose_name_plural=("Roles")

    def __str__(self):
        return self.name

class MyUser(AbstractBaseUser, PermissionsMixin):
    username=models.CharField(max_length=50)
    email=models.EmailField(
        verbose_name='email_address',
        max_length=250,
        unique=True,
    )
    date_of_birth=models.DateField()
    profile_image=models.ImageField(upload_to='profile_pics/', blank=True)
    about=models.TextField()
    groupe=GenericRelation("groups.Groupe")
    notif=GenericRelation("actions.Notification")
    following=models.ManyToManyField('self', through=Contact,
                                    related_name='followers',
                                    symmetrical=False)

    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)

    objects=MyUserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['date_of_birth', 'username']

    def __str__(self):
        return self.username

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
