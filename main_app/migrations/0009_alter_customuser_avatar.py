# Generated by Django 5.0.1 on 2024-01-22 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_customuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.URLField(default='https://mood-wave-avatars.s3.us-east-2.amazonaws.com/e9090c.jpeg'),
        ),
    ]