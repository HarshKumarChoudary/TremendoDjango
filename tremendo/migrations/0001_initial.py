# Generated by Django 3.1.5 on 2021-04-30 02:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalclasses', models.IntegerField()),
                ('completedclasses', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('address', models.TextField()),
                ('phone_no', models.IntegerField()),
                ('email', models.EmailField(max_length=250)),
                ('photo', models.ImageField(null=True, upload_to='productimg')),
                ('batchhandling', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tremendo.batch')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('address', models.TextField()),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=2)),
                ('email', models.EmailField(max_length=250)),
                ('photo', models.ImageField(null=True, upload_to='productimg')),
                ('batchenrolled', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tremendo.batch')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='batch',
            name='Student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tremendo.student'),
        ),
        migrations.AddField(
            model_name='batch',
            name='Teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tremendo.teacher'),
        ),
    ]