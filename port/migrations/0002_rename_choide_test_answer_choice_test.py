# Generated by Django 5.1.4 on 2025-01-06 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='choide_test',
            new_name='choice_test',
        ),
    ]