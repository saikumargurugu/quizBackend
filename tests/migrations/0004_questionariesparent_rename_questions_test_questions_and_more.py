# Generated by Django 4.1.4 on 2022-12-14 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_test_testscoresscores'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionariesParent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=500)),
            ],
        ),
        migrations.RenameField(
            model_name='test',
            old_name='Questions',
            new_name='questions',
        ),
        migrations.AddField(
            model_name='questionaries',
            name='questionaries_parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tests.questionariesparent'),
        ),
    ]
