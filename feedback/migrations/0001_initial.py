# Generated by Django 5.2 on 2025-05-05 17:49

import django.db.models.deletion
from django.db import migrations, models


def load_questions(apps, schema_editor):
    Question = apps.get_model('feedback', 'Question')
    questions = [
        "How satisfied are you with your overall experience at TECHZONE?",
        "How would you rate the quality of teaching at TECHZONE?",
        "Is your teacher punctual?",
        "How is the ambiance of TECHZONE?",
        "How satisfied are you with available resources and facilities at TECHZONE?",
        "How likely are you to recommend TECHZONE to others seeking educational opportunities?"
    ]
    for q in questions:
        Question.objects.create(question_text=q)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=20)),
                ('course_name', models.CharField(max_length=100)),
                ('teacher_name', models.CharField(max_length=100)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=15)),
                ('question', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='feedback.question')),
            ],
        ),
        migrations.CreateModel(
            name='StudentFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='feedback.choice')),
                ('question', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='feedback.question')),
                ('student', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='feedback.student')),
            ],
        ),
        migrations.RunPython(load_questions),
    ]
