# Generated by Django 3.0.5 on 2020-05-23 02:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='no title added', max_length=80)),
                ('body', models.TextField()),
                ('submitted_on', models.DateTimeField(auto_now_add=True)),
                ('retwitters', models.ManyToManyField(blank=True, related_name='questions_retwitted', to=settings.AUTH_USER_MODEL)),
                ('submitted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions_submitted', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-submitted_on',),
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('submitted_on', models.DateTimeField(auto_now_add=True)),
                ('replies', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quans.Answer')),
                ('reply_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='quans.Question')),
                ('submitted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answers', to=settings.AUTH_USER_MODEL)),
                ('user_upvote', models.ManyToManyField(related_name='answers_upvoted', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
