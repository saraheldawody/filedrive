# Generated by Django 2.2.13 on 2020-10-23 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='Content',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]