# Generated by Django 4.2.18 on 2025-03-09 21:40

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_alter_post_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="body",
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text"),
        ),
    ]
