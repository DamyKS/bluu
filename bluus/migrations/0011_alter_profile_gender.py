# Generated by Django 4.0.5 on 2022-06-27 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bluus', '0010_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=69, null=True),
        ),
    ]
