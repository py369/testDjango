# Generated by Django 5.1.4 on 2024-12-19 09:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_voetbalspelers'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Voetbalspelers',
            new_name='Voetbalspeler',
        ),
    ]
