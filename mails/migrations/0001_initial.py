# Generated by Django 4.1.7 on 2023-03-07 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("name", models.CharField(max_length=200, null=True)),
                ("email", models.CharField(max_length=200, null=True)),
                ("phone", models.CharField(max_length=200, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="IncomingMail",
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
                ("diary_no", models.IntegerField(null=True)),
                ("reference_no", models.CharField(max_length=200, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("from_city", models.CharField(max_length=200, null=True)),
                ("to_whom_marked", models.CharField(max_length=200)),
                ("annotation", models.CharField(max_length=200, null=True)),
                ("sign_by", models.CharField(max_length=200, null=True)),
                ("sign_date", models.CharField(max_length=200, null=True)),
                ("year_of_transcation", models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="OutgoingMail",
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
                ("diary_no", models.IntegerField(null=True)),
                ("reference_no", models.CharField(max_length=200, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("file_ref_date", models.CharField(max_length=200, null=True)),
                ("from_city", models.CharField(max_length=200, null=True)),
                ("subject", models.CharField(max_length=200, null=True)),
                ("disposal", models.CharField(max_length=200, null=True)),
                ("sign_by", models.CharField(max_length=200, null=True)),
                ("sign_date", models.CharField(max_length=200, null=True)),
                ("year_of_transcation", models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
