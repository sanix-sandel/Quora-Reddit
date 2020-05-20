from django.contrib import admin
from .models import Question, Answer, Group

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Group)
# Register your models here.
