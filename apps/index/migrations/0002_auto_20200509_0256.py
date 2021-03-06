# Generated by Django 3.0.5 on 2020-05-08 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=25, unique=True)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='experience',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='fio',
            field=models.CharField(default='-', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default='0', max_length=17),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.FileField(default='uploads/', upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
