# Generated by Django 3.0.5 on 2020-05-31 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quans', '0002_question_groupe'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]