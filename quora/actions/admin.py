from django.contrib import admin
from .models import Action, Notification

@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display=('user', 'verb', 'target', 'created')
    list_filter=('created',)
    search_fields=('verb',)

@admin.register(Notification)
class ActionAdmin(admin.ModelAdmin):
    list_display=('user', 'verb', 'target', 'created')
    list_filter=('created',)
    search_fields=('verb',)
