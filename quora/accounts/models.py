from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth=models.DateField(blank=True, null=True)
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"Profile for user {self.user.username}"
