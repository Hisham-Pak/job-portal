# Generated by Django 3.0.8 on 2020-10-22 14:29

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20201022_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='cv',
            field=models.FileField(null=True, storage=django.core.files.storage.FileSystemStorage(location='/media/files'), upload_to=''),
        ),
    ]
