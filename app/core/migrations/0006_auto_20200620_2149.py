# Generated by Django 2.1.15 on 2020-06-20 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='time',
            new_name='time_minutes',
        ),
    ]