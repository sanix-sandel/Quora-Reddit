import datetime
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from .models import Action, Notification

def create_action(user, verb, target=None):
    now=timezone.now()
    last_minute=now-datetime.timedelta(seconds=60)
    similar_actions=Action.objects.filter(user_id=user.id,
                                            verb=verb,
                                            created__gte=last_minute)
    if target:#It must be imporoved by using just target intead of
    #target_ct
        target_ct=ContentType.objects.get_for_model(target)
        #get the model of the target
        similar_actions=similar_actions.filter(
            target_ct=target_ct,
            target_id=target.id
        )
        #checking if the target is the same who made ealier actions
    if not similar_actions:
        #no existing similations actions found

        action=Action(user=user, verb=verb, target=target)
        action.save()
        return True
    return False


def create_notification(verb, target, user=None):
    if user!=target:
        notification=Notification(user=user, verb=verb, target=target)
        notification.save()

    else:
        return True
        #notification=Notification(user=None, verb=verb, target=target)
        #notification.save()
    return True
