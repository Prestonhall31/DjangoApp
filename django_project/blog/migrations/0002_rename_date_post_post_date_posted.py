# Generated by Django 4.2 on 2023-04-19 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_post',
            new_name='date_posted',
        ),
    ]