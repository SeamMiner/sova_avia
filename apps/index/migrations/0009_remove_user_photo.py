# Generated by Django 3.0.5 on 2020-05-09 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20200509_0319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='photo',
        ),
    ]
