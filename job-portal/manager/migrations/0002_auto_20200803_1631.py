# Generated by Django 3.0.8 on 2020-08-03 11:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cover_Letter',
            new_name='CoverLetter',
        ),
    ]
