from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Question(models.Model):
    title=models.CharField(max_length=80, default='no title added')
    body=models.TextField()
    submitted_by=models.ForeignKey(User, related_name='questions_submitted',
                                    on_delete=models.CASCADE)                             
    submitted_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"                      

    def get_absolute_url(self):
        return reverse('question', args=[self.id])
# Create your models here.
