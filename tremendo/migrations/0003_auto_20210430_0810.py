# Generated by Django 3.1.5 on 2021-04-30 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tremendo', '0002_auto_20210430_0758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='batchenrolled',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='batchhandling',
        ),
    ]
