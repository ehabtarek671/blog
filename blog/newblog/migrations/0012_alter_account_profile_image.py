# Generated by Django 5.1.5 on 2025-02-01 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newblog', '0011_alter_comment_author_alter_comment_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='../home/static/ProfileImages/<django.db.models.fields.CharField>'),
        ),
    ]
