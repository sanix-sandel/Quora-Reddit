from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from .models import Groupe, MembersRequested

@receiver(post_save, sender=Groupe)
def create_request_list(sender, instance, created, **kwargs):
    if created:
        MembersRequested.objects.create(groupe=instance)


@receiver(post_save, sender=Groupe)
def save_request_list(sender, instance, **kwargs):
    instance.members_request.save()
