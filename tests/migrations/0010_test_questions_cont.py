# Generated by Django 4.1.4 on 2022-12-15 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0009_remove_questionaries_question_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='questions_cont',
            field=models.IntegerField(default=0),
        ),
    ]
