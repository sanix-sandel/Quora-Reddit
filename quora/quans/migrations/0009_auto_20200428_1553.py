# Generated by Django 3.0.5 on 2020-04-28 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quans', '0008_answer_upvotes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='upvotes',
        ),
        migrations.AddField(
            model_name='answer',
            name='user_upvote',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers_upvoted', to=settings.AUTH_USER_MODEL),
        ),
    ]
