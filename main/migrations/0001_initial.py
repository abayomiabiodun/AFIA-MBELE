# Generated by Django 4.1.7 on 2023-04-14 20:47

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
            name='Service',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=40)),
                ('service_description', models.TextField(blank=True, null=True)),
                ('service_type', models.CharField(blank=True, choices=[('Health care service', 'Health Care'), ('Health Insurance service', 'Health Insurance'), ('Emmergency support', 'Emergency'), ('Aid', 'Aid'), ('Other', 'Other')], default='Health care service', max_length=45, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('avenue', models.CharField(max_length=25)),
                ('township', models.CharField(max_length=30)),
                ('town', models.CharField(max_length=25)),
                ('country', models.CharField(max_length=40)),
                ('longitute', models.CharField(max_length=25)),
                ('latitude', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('phone1', models.CharField(max_length=12)),
                ('phone2', models.CharField(max_length=12)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=20)),
                ('profile_pic', models.FileField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('avenue', models.CharField(max_length=25)),
                ('township', models.CharField(max_length=30)),
                ('town', models.CharField(max_length=25)),
                ('country', models.CharField(max_length=40)),
                ('longitute', models.CharField(max_length=25)),
                ('latitude', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('phone1', models.CharField(max_length=12)),
                ('phone2', models.CharField(max_length=12)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('organization_name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('organization_type', models.CharField(choices=[('Hospital', 'Hospital'), ('Drugstore', 'Drugstore'), ('Clinic', 'Clinic'), ('Dispensair', 'Dispensair'), ('Insurance institution', 'Insurance'), ('GOVENMENT', 'Govenment')], default='Hospital', max_length=40)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='oganisation_admin_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
