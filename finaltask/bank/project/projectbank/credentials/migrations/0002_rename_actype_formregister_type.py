# Generated by Django 4.1.7 on 2023-07-31 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formregister',
            old_name='actype',
            new_name='type',
        ),
    ]
