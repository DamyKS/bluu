# Generated by Django 4.0.5 on 2022-06-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bluus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(blank=True, default='01/01/2000'),
        ),
    ]
