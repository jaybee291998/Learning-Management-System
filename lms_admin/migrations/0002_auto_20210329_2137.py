# Generated by Django 3.1.4 on 2021-03-29 13:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lms_admin', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Admins',
            new_name='Admin',
        ),
    ]
