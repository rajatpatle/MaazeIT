# Generated by Django 4.1.3 on 2022-11-26 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crud_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='management',
            name='pan',
            field=models.FileField(default=True, upload_to='uploads/'),
        ),
    ]
