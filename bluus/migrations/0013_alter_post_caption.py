# Generated by Django 4.0.5 on 2022-07-03 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bluus', '0012_profile_relationship_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.TextField(blank=True, null=True),
        ),
    ]
