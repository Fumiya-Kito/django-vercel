# Generated by Django 4.2.1 on 2023-05-06 11:05

import datetime
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
            name='Shift',
            fields=[
                ('user_name', models.CharField(blank=True, max_length=50, null=True)),
                ('section', models.CharField(blank=True, max_length=50, null=True)),
                ('period_start', models.DateField()),
                ('period_end', models.DateField()),
                ('remarks', models.TextField(blank=True, null=True)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShiftItem',
            fields=[
                ('date', models.DateField()),
                ('day', models.CharField(blank=True, max_length=50, null=True)),
                ('is_work', models.BooleanField(default=False)),
                ('is_all_day', models.BooleanField(default=False)),
                ('start_time', models.TimeField(blank=True, default=datetime.time(8, 0))),
                ('end_time', models.TimeField(blank=True, default=datetime.time(3, 0))),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('shift', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.shift')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('section', models.CharField(blank=True, max_length=50, null=True)),
                ('duty', models.CharField(blank=True, max_length=50, null=True)),
                ('employment_status', models.CharField(blank=True, max_length=50, null=True)),
                ('is_rookie', models.BooleanField(default=True)),
                ('is_open_staff', models.BooleanField(default=False)),
                ('is_pre_close_staff', models.BooleanField(default=False)),
                ('is_close_staff', models.BooleanField(default=False)),
                ('start_default', models.TimeField(default=datetime.time(8, 0))),
                ('end_default', models.TimeField(default=datetime.time(17, 0))),
                ('desired_times_per_week', models.IntegerField(blank=True, default=0, null=True)),
                ('desired_working_time', models.IntegerField(blank=True, default=0, null=True)),
                ('commute', models.CharField(blank=True, max_length=50, null=True)),
                ('station', models.CharField(blank=True, max_length=50, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
