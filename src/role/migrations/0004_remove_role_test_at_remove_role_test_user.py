# Generated by Django 5.0 on 2023-12-25 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('role', '0003_role_test_at_role_test_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='test_at',
        ),
        migrations.RemoveField(
            model_name='role',
            name='test_user',
        ),
    ]