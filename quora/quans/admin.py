from django.contrib import admin
from .models import Question, Answer

admin.site.index_template='memcache_status/admin_index.html'

admin.site.register(Question)
admin.site.register(Answer)

# Register your models here.
