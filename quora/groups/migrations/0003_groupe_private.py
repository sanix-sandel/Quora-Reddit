# Generated by Django 3.0.5 on 2020-06-02 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20200527_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupe',
            name='private',
            field=models.BooleanField(default=False),
        ),
    ]