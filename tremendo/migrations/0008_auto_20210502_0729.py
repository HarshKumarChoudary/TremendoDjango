# Generated by Django 3.1.5 on 2021-05-02 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tremendo', '0007_auto_20210501_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=6, null=True),
        ),
    ]
