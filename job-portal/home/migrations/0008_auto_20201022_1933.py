# Generated by Django 3.0.8 on 2020-10-22 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20201022_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='cv',
            field=models.FileField(null=True, upload_to='media/'),
        ),
    ]