# Generated by Django 4.2.6 on 2023-12-08 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiTec', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='nombresApellidos',
        ),
    ]
