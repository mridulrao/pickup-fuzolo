# Generated by Django 4.2.6 on 2023-10-30 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_useraddpoints'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddpoints',
            name='comment',
            field=models.CharField(default='', max_length=255),
        ),
    ]