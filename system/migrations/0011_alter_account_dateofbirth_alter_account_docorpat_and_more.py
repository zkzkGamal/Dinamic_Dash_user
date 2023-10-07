# Generated by Django 4.1.1 on 2023-04-17 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0010_account_propic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='DateOfBirth',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='DocOrPat',
            field=models.TextField(blank=True, choices=[('doctor', 'doctor'), ('patient', 'patient')]),
        ),
        migrations.AlterField(
            model_name='account',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='fullName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='gender',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='payMethod',
            field=models.TextField(blank=True, choices=[('cash', 'cash'), ('paypal', 'paypal'), ('visa', 'visa')]),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='proPic',
            field=models.FileField(blank=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='account',
            name='specialList',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]