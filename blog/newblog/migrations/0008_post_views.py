# Generated by Django 5.1.5 on 2025-02-01 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newblog', '0007_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.BigIntegerField(default=0),
        ),
    ]
