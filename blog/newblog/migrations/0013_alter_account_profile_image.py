# Generated by Django 5.1.5 on 2025-02-01 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newblog', '0012_alter_account_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='../home/static/ProfileImages/<django.db.models.fields.EmailField>'),
        ),
    ]
