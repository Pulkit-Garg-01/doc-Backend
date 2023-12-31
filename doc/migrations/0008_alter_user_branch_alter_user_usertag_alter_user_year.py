# Generated by Django 4.2.6 on 2023-10-25 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doc", "0007_user_access_token_user_refresh_token"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="branch",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="userTag",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="year",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
