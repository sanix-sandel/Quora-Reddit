# Generated by Django 3.0.7 on 2020-07-03 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0009_auto_20200613_1841'),
        ('quans', '0004_auto_20200608_0718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shared',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('groupe', models.ManyToManyField(related_name='shared_questions', to='groups.Groupe')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shared_question', to='quans.Question')),
            ],
        ),
    ]