# Generated by Django 3.0.7 on 2020-07-12 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
        ('quans', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionrequestlist',
            name='questions',
            field=models.ManyToManyField(blank=True, related_name='groups_request', related_query_name='groups_request', to='quans.Question'),
        ),
        migrations.AddField(
            model_name='membersrequested',
            name='groupe',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='groups.Groupe'),
        ),
        migrations.AddField(
            model_name='membersrequested',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='groups_requested', related_query_name='groups_requested', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groupe',
            name='member',
            field=models.ManyToManyField(blank=True, related_name='a_group', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groupe',
            name='owner_ct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='own_group', to='contenttypes.ContentType'),
        ),
    ]