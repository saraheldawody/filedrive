# Generated by Django 2.2.13 on 2020-10-23 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0002_file_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Password',
            field=models.CharField(max_length=100),
        ),
    ]
