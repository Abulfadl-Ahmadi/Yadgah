# Generated by Django 4.2.17 on 2025-01-10 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0013_question_approved"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="question",
            name="approved",
        ),
        migrations.AddField(
            model_name="reply",
            name="approved",
            field=models.BooleanField(default=False),
        ),
    ]
