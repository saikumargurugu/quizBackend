# Generated by Django 4.1.4 on 2022-12-15 02:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0005_alter_test_completed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='exam_id',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
