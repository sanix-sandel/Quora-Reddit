from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Groupe(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    #We'll use ContentType rather than...
    owner_model=models.ForeignKey(ContentType, blank=True,
                            null=True, related_name='own_groupe',
                            on_delete=models.CASCADE)
    owner_id=models.PositiveIntegerField(null=True, blank=True)
    owner=GenericForeignKey('owner_model', 'owner_id')                   
    #owner=models.OneToOneField(settings.AUTH_USER_MODEL,
    #                            related_name='his_group',
    #                            on_delete=models.CASCADE)

    member=models.ManyToManyField(settings.AUTH_USER_MODEL,
                                related_name='a_group',
                                blank=True)

    def get_absolute_url(self):
        return reverse('groupe_detail', args=[self.id])

    def __str__(self):
        return f'{self.title}'
