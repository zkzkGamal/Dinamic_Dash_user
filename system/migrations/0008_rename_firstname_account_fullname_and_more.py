# Generated by Django 4.1.1 on 2023-04-17 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0007_account_dateofbirth_account_docorpat_account_country_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='firstName',
            new_name='fullName',
        ),
        migrations.RemoveField(
            model_name='account',
            name='lastName',
        ),
    ]
