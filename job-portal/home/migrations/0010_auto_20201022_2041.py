# Generated by Django 3.0.8 on 2020-10-22 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20201022_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
