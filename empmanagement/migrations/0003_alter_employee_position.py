# Generated by Django 5.1.4 on 2024-12-08 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empmanagement', '0002_rename_contact_employee_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('DEVELOPER', 'DEVELOPER'), ('HR MANAGER', 'HR MANAGER'), ('QUALITY ANALYST', 'QUALITY ANALYST'), ('UI_UX', 'UI_UX')], max_length=30),
        ),
    ]
