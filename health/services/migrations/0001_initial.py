# Generated by Django 2.2.5 on 2019-09-22 13:00

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
            name='ServiceProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last modified date')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=255, unique=True)),
                ('nature_of_emergency', models.CharField(choices=[('Accident', 'Accident'), ('Stroke', 'Stroke'), ('Fire', 'Fire'), ('Other', 'Other')], max_length=255)),
                ('preferred_choice', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last modified date')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('service_provider', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='services.ServiceProvider')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last modified date')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Question')),
            ],
        ),
    ]
