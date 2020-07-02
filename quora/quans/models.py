from django.conf import settings
from django.db import models
from django.urls import reverse


class QuestionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(groupe=None)



class Question(models.Model):
    title=models.CharField(max_length=80, default='no title added')
    body=models.TextField()
    available=models.BooleanField(default=True)
    submitted_by=models.ForeignKey(settings.AUTH_USER_MODEL,
                                    related_name='questions_submitted',
                                    on_delete=models.CASCADE)

    submitted_on=models.DateTimeField(auto_now_add=True)
    retwitters=models.ManyToManyField(
                                    settings.AUTH_USER_MODEL,
                                    related_name='questions_retwitted',
                                    blank=True,)

    groupe=models.ForeignKey("groups.Groupe", related_name='questions',
                            null=True, blank=True, on_delete=models.CASCADE)

    objects= QuestionManager()                       

    class Meta:
        ordering=('-submitted_on',)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('question', args=[self.id])


class Answer(models.Model):
    body=models.TextField()
    reply_to=models.ForeignKey(Question, related_name='answers',
                                on_delete=models.CASCADE)
    submitted_by=models.ForeignKey(settings.AUTH_USER_MODEL,
                                    related_name='user_answers',
                                    on_delete=models.CASCADE)
    submitted_on=models.DateTimeField(auto_now_add=True)
    replies=models.ForeignKey('self', blank=True, related_name='all_replies',
                                null=True, on_delete=models.CASCADE)
    user_upvote=models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='answers_upvoted')

    def __str__(self):
        return f"reply to {self.reply_to.title}"


     
class Shared(models.Model):
    parent=models.ForeignKey(Question, related_name='shared_question', 
        on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    groupe=models.ManyToManyField("groups.Groupe", related_name='shared_questions')

    def __str__(self):
        return f'shared of {self.parent.title}'    

