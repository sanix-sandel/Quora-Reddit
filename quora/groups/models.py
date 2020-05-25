from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


class Groupe(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    owner_ct=models.ForeignKey(ContentType, blank=True,
                                null=True,
                                related_name='own_group',
                                on_delete=models.CASCADE)
    owner_id=models.PositiveIntegerField(null=True, blank=True, db_index=True)
    owner=GenericForeignKey('owner_ct', 'owner_id')
    #An intermediary model must be added in order to associate the memeber and the group
    #so we can get information such the date of his joining
    member=models.ManyToManyField(settings.AUTH_USER_MODEL,
                                related_name='a_group',
                                blank=True)

    def get_absolute_url(self):
        return reverse('groupe_detail', args=[self.id])

    def __str__(self):
        return f'{self.title} owned by {self.owner}'
    
"""
class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
 """  
    
    
#owner=GenericRelat(settings.AUTH_USER_MODEL, related_query_name='own_group')
#We'll use ContentType rather than...
#owner_model=models.ForeignKey(ContentType, blank=False,
#                        null=False, related_name='own_groupe',
#                        on_delete=models.CASCADE)
#owner_id=models.PositiveIntegerField(null=False, blank=False, db_index=True)
#owner=GenericForeignKey('owner_model', 'owner_id')
#owner=models.OneToOneField(settings.AUTH_USER_MODEL,
#                            related_name='his_group',
#                            on_delete=models.CASCADE)
