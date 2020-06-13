from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from .models import Groupe, MembersRequested, QuestionRequestList

@receiver(post_save, sender=Groupe)
def create_groupe(sender, instance, created, **kwargs):
    if created:
        QuestionRequestList.objects.create(groupe=instance)
        MembersRequested.objects.create(groupe=instance)


@receiver(post_save, sender=Groupe)
def save_groupe(sender, instance, **kwargs):
    instance.membersrequested.save()
    instance.questionrequestlist.save()
