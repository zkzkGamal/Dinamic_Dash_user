# Generated by Django 4.1.1 on 2023-06-10 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0013_remove_account_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='username',
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
