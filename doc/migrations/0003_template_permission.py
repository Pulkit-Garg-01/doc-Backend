# Generated by Django 4.2.4 on 2023-10-07 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("doc", "0002_group_document_content_user_enrollmentno_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="template",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("content", models.TextField()),
                (
                    "createdBy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="doc.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="permission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "permission",
                    models.CharField(
                        choices=[("R", "Read only"), ("RW", "Read and Write")],
                        max_length=2,
                    ),
                ),
                (
                    "docId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="doc.document"
                    ),
                ),
                (
                    "userId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="doc.user"
                    ),
                ),
            ],
        ),
    ]
