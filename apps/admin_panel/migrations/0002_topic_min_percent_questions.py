# Generated by Django 3.0.5 on 2020-05-09 08:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='min_percent_questions',
            field=models.PositiveSmallIntegerField(default=50),
            preserve_default=False,
        ),
    ]
