# Generated by Django 4.1.1 on 2023-04-17 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('system', '0004_alter_draft_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draft',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
