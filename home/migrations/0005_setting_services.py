# Generated by Django 3.1.7 on 2021-05-29 14:42

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210526_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='services',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
