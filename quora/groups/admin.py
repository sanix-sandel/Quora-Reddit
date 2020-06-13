from django.contrib import admin
from .models import Groupe, MembersRequested, QuestionRequestList

admin.site.register(Groupe)
admin.site.register(MembersRequested)
admin.site.register(QuestionRequestList)
