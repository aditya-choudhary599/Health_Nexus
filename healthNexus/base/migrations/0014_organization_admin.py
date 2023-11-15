# Generated by Django 4.2.3 on 2023-11-15 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_patient_history_staff_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization_Admin',
            fields=[
                ('unique_id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('organization_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.organization')),
            ],
        ),
    ]
