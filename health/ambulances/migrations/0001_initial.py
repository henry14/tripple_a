# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-09-29 12:42
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('viewflow', '0008_merge'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverAssignmentProcess',
            fields=[
                ('subprocess_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='viewflow.Subprocess')),
                ('rejecting_drivers', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('viewflow.subprocess',),
        ),
        migrations.CreateModel(
            name='EmergencyAssessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(default='', max_length=255, verbose_name='At least two cell phone contacts separated by commas')),
                ('location', models.CharField(max_length=255)),
                ('short_notes', models.CharField(max_length=500)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyProcess',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='viewflow.Process')),
                ('point', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
                ('nature_of_emergency', models.CharField(choices=[('Accident', 'Accident'), ('Stroke', 'Stroke'), ('Fire', 'Fire'), ('Other', 'Other')], max_length=255)),
                ('question_answer', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('accept', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('viewflow.process',),
        ),
        migrations.AddField(
            model_name='emergencyassessment',
            name='emergency_process',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ambulances.EmergencyProcess'),
        ),
        migrations.AddField(
            model_name='driverassignmentprocess',
            name='emergency_process',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ambulances.EmergencyProcess'),
        ),
    ]
