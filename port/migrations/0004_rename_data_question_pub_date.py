# Generated by Django 5.1.4 on 2025-01-06 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0003_alter_question_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='data',
            new_name='pub_date',
        ),
    ]
