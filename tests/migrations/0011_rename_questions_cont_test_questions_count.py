# Generated by Django 4.1.4 on 2022-12-15 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0010_test_questions_cont'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='questions_cont',
            new_name='questions_count',
        ),
    ]
