# Generated by Django 5.1.4 on 2025-01-25 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='uuid',
            field=models.UUIDField(null=True),
        ),
    ]
