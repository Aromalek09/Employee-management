# Generated by Django 5.1.4 on 2024-12-07 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empmanagement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Contact',
            new_name='contact',
        ),
    ]
