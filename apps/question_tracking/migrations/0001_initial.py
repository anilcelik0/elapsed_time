# Generated by Django 5.0.1 on 2024-01-09 20:25

import apps.question_tracking.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apps', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionMainTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('color', models.CharField(default=apps.question_tracking.models.random_rgb, max_length=20)),
                ('target', models.IntegerField(blank=True, null=True)),
                ('target_is_complated', models.BooleanField(default=False)),
                ('main_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_main_topic', to='apps.maintopic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionSubTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('color', models.CharField(default=apps.question_tracking.models.random_rgb, max_length=20)),
                ('main_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_main', to='question_tracking.questionmaintopic')),
                ('sub_topic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_sub', to='apps.subtopic')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('question_count', models.IntegerField(blank=True, null=True)),
                ('correct_answer', models.IntegerField(blank=True, null=True)),
                ('wrong_answer', models.IntegerField(blank=True, null=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic', to='question_tracking.questionsubtopic')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]