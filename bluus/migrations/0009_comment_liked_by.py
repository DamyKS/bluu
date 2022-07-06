# Generated by Django 4.0.5 on 2022-06-27 20:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bluus', '0008_alter_profile_cover_photo_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='liked_by',
            field=models.ManyToManyField(related_name='likes_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]