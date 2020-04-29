from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Question(models.Model):
    title=models.CharField(max_length=80, default='no title added')
    body=models.TextField()
    submitted_by=models.ForeignKey(User, related_name='questions_submitted',
                                    on_delete=models.CASCADE)                             
    submitted_on=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('-submitted_on',)

    def __str__(self):
        return f"{self.title}"                      

    def get_absolute_url(self):
        return reverse('question', args=[self.id])


class Answer(models.Model):
    body=models.TextField()
    reply_to=models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    submitted_by=models.ForeignKey(User, related_name='user_answers', on_delete=models.CASCADE)
    submitted_on=models.DateTimeField(auto_now_add=True)
    replies=models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    user_upvote=models.ManyToManyField(User, related_name='answers_upvoted')

    def __str__(self):
        return f"reply to {self.reply_to.title}"

# Create your models here.
