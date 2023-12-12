# Generated by Django 4.2.6 on 2023-10-20 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doc", "0004_alter_user_options_alter_user_managers_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="email address"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=128, verbose_name="password"),
        ),
    ]
