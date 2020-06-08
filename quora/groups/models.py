from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


class Groupe(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    private=models.BooleanField(default=False)
    owner_ct=models.ForeignKey(ContentType, blank=False,
                                null=False,
                                related_name='own_group',
                                on_delete=models.CASCADE)
    owner_id=models.PositiveIntegerField(null=False, blank=False, db_index=True)
    owner=GenericForeignKey('owner_ct', 'owner_id')
    member=models.ManyToManyField(settings.AUTH_USER_MODEL,
                                related_name='a_group',
                                blank=True)

    actions=GenericRelation("actions.Action", related_query_name='actions')#because group may be a target

    def get_absolute_url(self):
        return reverse('groupe_detail', args=[self.id])

    def __str__(self):
        return f'{self.title} owned by {self.owner}'
