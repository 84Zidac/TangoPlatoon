# Generated by Django 4.1.7 on 2023-03-14 16:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("school_roster_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="students",
            name="age",
            field=models.IntegerField(default=0),
        ),
    ]
