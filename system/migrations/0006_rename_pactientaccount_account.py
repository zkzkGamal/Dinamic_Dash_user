# Generated by Django 4.1.1 on 2023-04-17 10:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('system', '0005_alter_draft_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='pactientaccount',
            new_name='account',
        ),
    ]
