from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Groupe(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    owner=models.OneToOneField(User, related_name='his_group', on_delete=models.CASCADE)
    member=models.ManyToManyField(User, related_name='a_group', blank=True)

    def get_absolute_url(self):
        return reverse('groupe_detail', args=[self.id])

    def __str__(self):
        return f'{self.title}'
